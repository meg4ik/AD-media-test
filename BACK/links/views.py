from django.utils.timezone import now, timedelta
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from user_agents import parse
from django.db.models import Count
from django.utils.dateparse import parse_date
from django.db.models import Sum, F

from advertising.models import Offer, Lead, Click, LeadCampaignInterest
from .utils import get_user_ip, get_geolocation

class RedirectView(APIView):
    def get(self, request, local_url, format=None):
        offer = get_object_or_404(Offer, local_url=local_url)

        user_ip = get_user_ip(request)
        geolocation = get_geolocation(user_ip)

        user_agent_string = request.META.get('HTTP_USER_AGENT', 'unknown')
        user_agent = parse(user_agent_string)
        browser = f'{user_agent.browser.family} {user_agent.browser.version_string}'
        os = f'{user_agent.os.family} {user_agent.os.version_string}'

        lead, created = Lead.objects.get_or_create(ip_address=user_ip)
        
        click = Click.objects.create(
            offer=offer,
            lead=lead,
            browser=browser,
            os=os,
            ip_address=user_ip,
            geolocation=geolocation
        )

        campaign = offer.campaign
        lead_campaign_interest, created = LeadCampaignInterest.objects.get_or_create(lead=lead, campaign=campaign)
        if lead_campaign_interest.interest_score < 5:
            lead_campaign_interest.interest_score += 1
        lead_campaign_interest.save()

        return redirect(offer.redirect_url)

class ClicksGraphView(APIView):
    def get(self, request, format=None):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        if start_date and end_date:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
            clicks = Click.objects.filter(timestamp__range=[start_date, end_date])
        else:
            last_30_days = now() - timedelta(days=30)
            clicks = Click.objects.filter(timestamp__gte=last_30_days)
        
        clicks = clicks.extra({'day': 'date(timestamp)'}).values('day').annotate(count=Count('id')).order_by('day')
        
        return Response(clicks)
    

class LeadsGraphView(APIView):
    def get(self, request, format=None):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        if start_date and end_date:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
            leads = Lead.objects.filter(created_at__range=[start_date, end_date])
        else:
            last_30_days = now() - timedelta(days=30)
            leads = Lead.objects.filter(created_at__gte=last_30_days)
        
        leads = leads.extra({'day': 'date(created_at)'}).values('day').annotate(count=Count('id')).order_by('day')
        
        return Response(leads)
    

class ConversionGraphView(APIView):
    def get(self, request, format=None):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        if start_date and end_date:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
            clicks = Click.objects.filter(timestamp__range=[start_date, end_date])
            leads = Lead.objects.filter(created_at__range=[start_date, end_date])
        else:
            last_30_days = now() - timedelta(days=30)
            clicks = Click.objects.filter(timestamp__gte=last_30_days)
            leads = Lead.objects.filter(created_at__gte=last_30_days)
        
        clicks_per_day = clicks.extra({'day': 'date(timestamp)'}).values('day').annotate(count=Count('id')).order_by('day')
        leads_per_day = leads.extra({'day': 'date(created_at)'}).values('day').annotate(count=Count('id')).order_by('day')

        conversion_data = []
        for click, lead in zip(clicks_per_day, leads_per_day):
            day = click['day']
            click_count = click['count']
            lead_count = lead['count'] if click['day'] == lead['day'] else 0
            conversion_rate = lead_count / click_count if click_count > 0 else 0
            conversion_data.append({'day': day, 'conversion_rate': conversion_rate})

        return Response(conversion_data)


class RevenueGraphView(APIView):

    def get(self, request, *args, **kwargs):
        campaign_id = request.query_params.get('campaign_id')
        if campaign_id:
            revenue_data = Click.objects.filter(offer__campaign_id=campaign_id).values(day=F('timestamp__date')).annotate(revenue=Sum(F('offer__click_price')))
        else:
            revenue_data = Click.objects.values(day=F('timestamp__date')).annotate(revenue=Sum(F('offer__click_price')))
        
        data = [{"day": entry["day"], "revenue": entry["revenue"]} for entry in revenue_data]

        return Response(data)