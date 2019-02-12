import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.views import rotate_image

# Create your models here.
class make(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=False)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    summary=models.TextField(blank=True,null=False)
    featured=models.BooleanField(default=True)
    image=models.ImageField(upload_to='image')
    shared=models.BooleanField(default=False)


