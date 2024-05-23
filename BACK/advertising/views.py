
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Campaign, Offer, Lead, Click
from .serializers import CampaignSerializer, OfferSerializer, LeadSerializer, ClickSerializer
from .filters import ClickFilter


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['start_date', 'end_date']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'campaign__name']
    ordering_fields = ['name', 'click_price']


class LeadViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['ip_address', 'created_at']
    

class ClickViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['timestamp', 'ip_address']