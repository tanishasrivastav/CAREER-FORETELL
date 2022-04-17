from operator import mod
from django.db import models

# Create your models here.

class Blog(models.Model):
    blogID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    metadetail = models.CharField(max_length=100)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blogs/thumbnail', blank=True, null=True)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    subject = models.CharField(max_length=100)
    message = models.TextField()