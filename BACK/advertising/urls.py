from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, OfferViewSet, LeadViewSet, ClickViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'clicks', ClickViewSet)

urlpatterns = [

]
urlpatterns += router.urls