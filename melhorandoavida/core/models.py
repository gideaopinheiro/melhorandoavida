from django.db import models
from slugify import slugify

# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=256, null=True)
    username = models.CharField(unique=True, max_length=256, blank=True, null=True)

    ocupation = models.CharField(max_length=256, blank=True, null=True)
    university = models.CharField(max_length=256, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    
    