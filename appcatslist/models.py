from django.db import models

# Create your models here.

cities = (
        ('greenville', 'Greenville'),
        ('charleston', 'Charleston'),
        ('ashville', 'Asheville'),
        ('atlanta', 'Atlanta')
        )


class UserProfile(models.Model):
    user = models.OneToOneField('auth.user')
    username = models.CharField(max_length=30)
    preferredcity = models.CharField(max_length=30, choices=cities, null=True)
    profilepicture = models.ImageField(upload_to='profile_photos', null=True, blank=True, name='profile photo')
