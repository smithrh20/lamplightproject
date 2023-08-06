from django.contrib import admin
from django.contrib.auth.models import User
from pyexpat import model
from unicodedata import name
from django.db import models
from django.db import models
from django.urls import reverse

class Camera(models.Model):
    name = models.CharField(max_length=255)

class Photo(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to='images/')
    name = models.CharField(max_length=100)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    f_Stop = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url