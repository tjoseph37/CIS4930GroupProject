# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

from django.db import models


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = "profile"

class Flowers(models.Model):
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_at=models.DateTimeField(default=datetime.now, blank=True)

	def _str_(self):
		return self.title




