from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from user_agents import parse

from advertising.models import Offer, Lead, Click

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

        return redirect(offer.redirect_url)
