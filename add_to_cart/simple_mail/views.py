from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
from django.core.mail import send_mail
# Create your views here.

def email(request):
    
    send_mail('Yo Yo!!!', 'If you are reading this, it worked!', 'patrickfalvey40@gmail.com', ['patrickfalvey40@gmail.com'])
    return HttpResponse('Your email has been sent!')
