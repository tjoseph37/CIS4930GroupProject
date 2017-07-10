# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


#Index presents homepage to user 
def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

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


def contact(request):
    form_class = ContactForm
	#If form submitted, check that valid form was sent and each feild has valid data
    if request.method == 'POST':
        form = form_class(data=request.POST)
	
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Send contact form info to email 
            template = get_template('contact_template.txt')
	    
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
	    #content=render_to_string("contact_template.txt",context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "Flowers" +'',
                ['tj14@my.fsu.edu'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })

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
