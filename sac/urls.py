from django.urls import path
from sac.views import home, complaint, sobre


urlpatterns = [
    path('', home),
    path('complaint/', complaint),
    path('SOBRE/', sobre),
]
