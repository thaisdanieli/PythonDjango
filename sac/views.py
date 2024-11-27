from django.shortcuts import render # lê o arquivo e renderiza
from django.http import HttpResponse

# Create your views here.

# HTTP REQUEST
def home(request):
    return render(request, 'sac/home.html', context={'name': 'Thais Danieli', })

#Return HTTP Response
def complaint(request):
    return render(request, 'sac/complaint.html')

# HTTP REQUEST
def sobre(request):
    return HttpResponse('SOBRE')