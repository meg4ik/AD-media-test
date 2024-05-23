import django_filters
from .models import Campaign, Offer, Lead, Click, LeadCampaignInterest

class OfferFilter(django_filters.FilterSet):
    class Meta:
        model = Offer
        fields = ['name', 'campaign']

class LeadFilter(django_filters.FilterSet):
    class Meta:
        model = Lead
        fields = ['ip_address']

class ClickFilter(django_filters.FilterSet):
    class Meta:
        model = Click
        fields = ['offer', 'lead', 'timestamp']

class LeadCampaignInterestFilter(django_filters.FilterSet):
    class Meta:
        model = LeadCampaignInterest
        fields = ['lead', 'campaign', 'interest_score']
