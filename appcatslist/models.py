from django.db import models
from django.contrib.auth.models import User

# Create your models here.

cities = (
        ('greenville', 'Greenville'),
        ('charleston', 'Charleston'),
        ('ashville', 'Asheville'),
        ('atlanta', 'Atlanta')
        )

categories = (
        ('item', 'Item'),
        ('service', 'Service'),
        )


class UserProfile(models.Model):
    user = models.OneToOneField('auth.user')
    username = models.CharField(max_length=30)
    preferredcity = models.CharField(max_length=30, choices=cities, null=True, blank=True)
    profilepicture = models.ImageField(upload_to='profile_photos', null=True, blank=True, name='profile photo')


class OfferPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=20, choices=categories)
    location = models.CharField(max_length=20, choices=cities)
