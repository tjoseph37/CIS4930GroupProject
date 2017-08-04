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
from flowers.forms import ProfileForm
from flowers.models import *
import tensorflow as tf
import sys
import os
import StringIO
import json
import c

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

def signup(request):
   if request.method == "POST":
        form = UserForm(request.POST)
 	username=form.cleaned_data['username']
        email= form.cleaned_data['email']
	password=form.clean_data['password']
        new_user = User(username=username, email=email, password=password)#.objects.create_user(**form.cleaned_data)
        login(new_user)
	new_user.save()
            # redirect, or however you want to get to the main view
        return HttpResponseRedirect('index.html')
   else:
        form = UserForm() 
   return render(request, 'signup.html',{'form': form} )
 

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
                send_mail(subject, message, from_email, ['FlowerProject4930@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return render(request, 'success.html')

#Class used to upload images and identity

def encrypt(data):
	client = c.ChatClient(1,data)
	return client.cmdloop()

def SaveProfile(request):
   saved = False
   human_string = "DEFAULT"
   MyProfileForm = "TESTING"
   #image_data=""
   if request.method == "POST":
      human_string = "First conditonal"
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      image_path = request.FILES['picture']
      # Read in the image_data
      # image_data = tf.gfile.FastGFile(image_path, 'rb').read()
      image_data = request.FILES['picture']
      # Loads label file, strips off carriage return
      label_lines = [line.rstrip() for line in open("{}/flowers/retrained_labels.txt".format(os.getcwd()), "r+")]
      
      with open("{}/flowers/retrained_graph.pb".format(os.getcwd()), 'rb') as f:
          graph_def = tf.GraphDef()
          graph_def.ParseFromString(f.read())
          tf.import_graph_def(graph_def, name='')
     
      # Feed the image_data as input to the graph and get first prediction
      with tf.Session() as sess:
	  softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	  # predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data.file})
       # Sort to show labels of first prediction in order of confidence
      # html=html+"test2"
     
      # top_k = predictions[0].argsort()[-len(predictions[0]):][::-1][0]
      human_string = str(type(image_data.file))
      # human_string = label_lines[top_k]
      # score = predictions[0][top_k]
      saved = True
     
   else:
      #MyProfileForm = Profileform()
      human_string = "Invalid form profile"
   #encrypt_data=encrypt(image_data.file.getvalue())
 
   html=""""<html><title>Upload Image</title><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\"><link rel=\"stylesheet\" href=\"https://www.w3schools.com/lib/w3-theme-black.css\">
<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Roboto\">
<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">
<style>
html,body,h1,h2,h3,h4,h5,h6 {font-family: \"Roboto\", sans-serif}
</style>
<body bgcolor=\"#40E0D0\">

<div class=\"w3-top\">
  <div class=\"w3-bar w3-theme w3-top w3-left-align w3-large\">
    <a class=\"w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1\" href=\"javascript:void(0)\" onclick=\"w3_open()\"><i class=\"fa fa-bars\"></i></a>
    <a href=\"#\" class=\"w3-bar-item w3-button w3-theme-l1">Flower App</a>
    <a href=\"http://127.0.0.1:8000\" class=\"w3-bar-item w3-button w3-hide-small w3-hover-white\">Homepage</a>
    <a href=\"http://127.0.0.1:8000/flowers\" class=\"w3-bar-item w3-button w3-hide-small w3-white\">Upload and Identify Flower</a>
    <a href=\"http://127.0.0.1:8000/encrypt\" class=\"w3-bar-item w3-button w3-hide-small w3-hover-white\">Encrypt Flower</a>
    <a href=\"http://127.0.0.1:8000/signup\" class=\"w3-bar-item w3-button w3-hide-small w3-hide-medium w03-hover-white\">Sign up</a>
    <a href=\"http://127.0.0.1:8000/about\" class=\"w3-bar-item w3-button w3-hide-small w3-hide-medium w3-hover-white\">About</a>
    <a href=\"http://127.0.0.1:8000/contact\" class=\"w3-bar-item w3-button w3-hide-small w3-hide-medium w3-hover-white\">Contact</a>
  </div>
</div>

<nav class=\"w3-sidebar w3-bar-block w3-collapse w3-large w3-theme-l5 w3-animate-left\" style=\"z-index:3;width:250px;margin-top:43px;\" id=\"mySidebar\">
  <a href=\"javascript:void(0)\" onclick=\"w3_close()\" class=\"w3-right w3-xlarge w3-padding-large w3-hover-black w3-hide-large\" title=\"Close Menu\">
    <i class=\"fa fa-remove\"></i>
  </a>
  <h4 class=\"w3-bar-item\"><b>Menu</b></h4>
  <a class=\"w3-bar-item w3-button w3-hover-black\" href=\"http://127.0.0.1:8000\">Homepage</a>
  <a class=\"w3-bar-item w3-button w3-hover-black\" href=\"http://127.0.0.1:8000/flowers\">Upload and Identify Flower</a>
  <a class=\"w3-bar-item w3-button w3-hover-black\" href=\"http://127.0.0.1:8000/encrypt\">Encrypt Flower</a>
  <a class=\"w3-bar-item w3-button w3-hover-black\" href=\"http://127.0.0.1:8000/signup\">Sign up</a>
  <a class=\"w3-bar-item w3-button w3-hover-black\" href=\"http://127.0.0.1:8000/about\">About</a>
  <a class=\"w3-bar-item w3-button w3-hover-black\" href=\"http://127.0.0.1:8000/contact\">Contact</a>
</nav>
<div class=\"w3-overlay w3-hide-large\" onclick=\"w3_close()\" style=\"cursor:pointer\" title=\"close side menu\" id=\"myOverlay\"></div>
<div class=\"w3-main\" style=\"margin-left:250px\">
<div class=\"w3-row w3-padding-64\">
</div>
<h1>Upload an Image!</h1>
<h4>Your flower image was identified as: </h4>
 <div class=\"container\">  
 <html><body><h3>%s </h3> </body></html>
<p><a href=\"http://127.0.0.1:8000\">Return to home</a></p>
  
</div>
<div class=\"w3-row w3-padding-64\">
</div>
<div class=\"w3-row w3-padding-64\">
</div>
  <footer id=\"myFooter">
    <div class=\"w3-container w3-theme-l2 w3-padding-32\">
      <h4>Flower App Project for Cis4930 Summer 2017</h4>
    </div>

    <div class=\"w3-container w3-theme-l1\">
      
    </div>
  </footer>
</div>
<script>
// Get the Sidebar
var mySidebar = document.getElementById(\"mySidebar\");

var overlayBg = document.getElementById(\"myOverlay\");

function w3_open() {
    if (mySidebar.style.display === \'block\') {
        mySidebar.style.display = \'none\';
        overlayBg.style.display = \"none\";
    } else {
        mySidebar.style.display = 'block';
        overlayBg.style.display = \"block\";
    }
}

function w3_close() {
    mySidebar.style.display = \"none\";
    overlayBg.style.display = \"none\";
}</script></body></html>""" % human_string
  
   return  HttpResponse(html)

#Encryption 
def SaveEncrypt(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = Profileform()
		
   return render(request, 'saveEncrypt.html', locals())
