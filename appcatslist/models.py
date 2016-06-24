from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    userdescription = models.TextField(null=True, blank=True)
    preferredcity = models.CharField(max_length=30, choices=cities, null=True, blank=True)
    # profilepicture = models.ImageField(upload_to='profile_photos', null=True, blank=True, name='profile photo')


class CategoryList(models.Model):
    category = models.CharField(max_length=50, choices=categories)


class City(models.Model):
    city = models.CharField(max_length=50)


class OfferPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(CategoryList)
    city = models.ForeignKey(City)


@receiver(post_save, sender='auth.user')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        UserProfile.objects.create(user=instance)
