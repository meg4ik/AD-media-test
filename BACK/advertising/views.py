
from rest_framework import mixins, viewsets


from .models import Campaign, Offer, Lead, Click
from .serializers import CampaignSerializer, OfferSerializer, LeadSerializer, ClickSerializer


class ReadOnlyCreateDestroyModelViewSet(viewsets.GenericViewSet, 
                                        mixins.CreateModelMixin, 
                                        mixins.RetrieveModelMixin, 
                                        mixins.DestroyModelMixin):
    pass


class CampaignViewSet(ReadOnlyCreateDestroyModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class OfferViewSet(ReadOnlyCreateDestroyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class LeadViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    

class ClickViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer