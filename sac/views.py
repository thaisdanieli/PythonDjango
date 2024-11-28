from django.shortcuts import render # lê o arquivo e renderiza
from django.http import HttpResponse

# Create your views here.

#Return HTTP Response
def home(request):
    return render(request, 'sac/home.html', context={'name': 'Thais Danieli', })


