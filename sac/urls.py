from django.urls import path
from sac.views import home


urlpatterns = [
    path('', home, name='home'),
]
