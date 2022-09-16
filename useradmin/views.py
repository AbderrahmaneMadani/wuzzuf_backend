from django.shortcuts import render
from django.http import HttpResponse
from . models import Useradmin

# Create your views here.

def index(request):

    return HttpResponse('hello user Admin')
def useradmin(request):
    return render (request, 'pages/useradmin.html')
def useradmins(request):
    return render (request, 'pages/useradmins.html', {'admin':Useradmin.objects.all()})
