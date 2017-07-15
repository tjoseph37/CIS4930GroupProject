# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError

#Index presents homepage to user 
def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')

def flowers(request):
	return render(request, 'flower.html')

def encrypt(request):
	return render(request, 'encrypt.html')

def page2(request):
	return render(request, 'page2.html')

def bluetooth(request):
	return render(request, 'bluetooth.html')

def page3(request):
	return render(request, 'page3.html')

def page4(request):
	return render(request, 'page4.html')

def page5(request):
	return render(request, 'page5.html')

#Connects to backend email server using mailgun
#Username: FlowerProject4930@gmail.com
#Password: cis4930flower

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['tj14@my.fsu.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return render(request, 'success.html')

#Class used to upload images 
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
