from django.urls import path

from .views import RedirectView

urlpatterns = [
    path('r/<str:local_url>/', RedirectView.as_view(), name='redirect'),
]