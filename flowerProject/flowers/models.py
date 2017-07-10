# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


# Create your models here.
class Flowers(models.Model):
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_at=models.DateTimeField(default=datetime.now, blank=True)

	def _str_(self):
		return self.title

class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'media/', default = '')


