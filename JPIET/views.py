from django.shortcuts import render, redirect
import smtplib
from email.message import EmailMessage
from django.http import HttpResponse

from frontend import models as fro_models


def home(request):

    home_image = fro_models.HomeImage.objects.get(uid__exact=1)
    return render(request, 'home.html', {'home_image':home_image})

def fault(request, fault):
    
    return render(request, 'fault.html', {'fault': fault})

def success(request, success):
    
    return render(request, 'success.html', {'success': success})