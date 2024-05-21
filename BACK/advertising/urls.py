from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, OfferViewSet, LeadViewSet, RedirectView

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'leads', LeadViewSet)

urlpatterns = [
    path('r/<str:local_url>/', RedirectView.as_view(), name='redirect'),
]
urlpatterns += router.urls