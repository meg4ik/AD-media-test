
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Campaign, Offer, Lead, Click
from .serializers import CampaignSerializer, OfferSerializer, LeadSerializer, ClickSerializer
from .filters import CampaignFilter, OfferFilter, LeadFilter, ClickFilter, LeadCampaignInterestFilter


class ReadOnlyCreateDestroyModelViewSet(viewsets.GenericViewSet, 
                                        mixins.CreateModelMixin, 
                                        mixins.RetrieveModelMixin, 
                                        mixins.DestroyModelMixin):
    pass


class CampaignViewSet(ReadOnlyCreateDestroyModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CampaignFilter


class OfferViewSet(ReadOnlyCreateDestroyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfferFilter


class LeadViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LeadFilter
    

class ClickViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClickFilter