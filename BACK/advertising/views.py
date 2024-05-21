from django.shortcuts import get_object_or_404, redirect
from rest_framework import mixins, viewsets
from rest_framework.views import APIView

from .models import Campaign, Offer, Lead
from .serializers import CampaignSerializer, OfferSerializer, LeadSerializer

from .utils import get_user_ip

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


class RedirectView(APIView):
    def get(self, request, local_url, format=None):
        offer = get_object_or_404(Offer, local_url=local_url)
        
        lead = Lead.objects.create(
            offer=offer,
            browser=request.META.get('HTTP_USER_AGENT', 'unknown'),
            os=request.META.get('HTTP_USER_AGENT', 'unknown'),
            ip_address=get_user_ip(request),
            geolocation='unknown'  # Геолокацию можно определить с помощью внешнего API
        )

        return redirect(offer.redirect_url)