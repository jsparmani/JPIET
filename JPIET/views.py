from django.shortcuts import render, redirect
import smtplib
from email.message import EmailMessage
from django.http import HttpResponse

from frontend import models as fro_models


def home(request):

    home_image = fro_models.HomeImage.objects.get(uid__exact=1)
    stats = fro_models.Statistics.objects.get(uid__exact=1)
    notices = fro_models.Notice.objects.all().filter(on_landing__exact=True)
    medias = fro_models.Media.objects.all().filter(on_landing__exact=True)
    events = fro_models.Event.objects.all().filter(on_landing__exact=True)
    testimonials = fro_models.Testimonial.objects.all()
    recruiters = fro_models.Recruiter.objects.all().filter(on_landing__exact=True)
    about_us = fro_models.Message.objects.get(uid__exact=1)
    home_pdf = fro_models.HomePDF.objects.get(uid__exact=1)
    
    return render(request, 'home.html', {'home_image':home_image, 'stats':stats, 'notices':notices, 'medias':medias, 'events':events, 'testimonials':testimonials, 'recruiters':recruiters, 'about_us':about_us, 'home_pdf':home_pdf})

def fault(request, fault):
    
    return render(request, 'fault.html', {'fault': fault})

def success(request, success):
    
    return render(request, 'success.html', {'success': success})