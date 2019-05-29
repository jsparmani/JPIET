from django.shortcuts import render, redirect
import smtplib
from email.message import EmailMessage
from django.http import HttpResponse

""" def email_check(request):



    msg = EmailMessage()
    msg['Subject'] = 'Trial Mail'
    msg['From'] = 'jpietuniversity@gmail.com'
    msg['To'] = 'sjparmani@gmail.com'
    msg.set_content('How about using gmail for SMTP')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login('jpietuniversity@gmail.com', 'cook!es123')

        smtp.send_message(msg)

    return HttpResponse('Sent') """


def home(request):
    
    return render(request, 'home.html')

def fault(request, fault):
    
    return render(request, 'fault.html', {'fault': fault})

def success(request, success):
    
    return render(request, 'success.html', {'success': success})