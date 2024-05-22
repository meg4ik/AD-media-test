from django.urls import path

from .views import RedirectView, ClicksGraphView, LeadsGraphView, ConversionGraphView

urlpatterns = [
    path('r/<str:local_url>/', RedirectView.as_view(), name='redirect'),
    path('graphs/clicks/', ClicksGraphView.as_view(), name='clicks-graph'),
    path('graphs/leads/', LeadsGraphView.as_view(), name='leads-graph'),
    path('graphs/conversions/', ConversionGraphView.as_view(), name='conversion-graph'),
]