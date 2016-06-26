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
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True, name='photo')

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons-256/rounded-glossy-black-icons-animals/016581-rounded-glossy-black-icon-animals-animal-cat4.png"


class CategoryList(models.Model):
    category = models.CharField(max_length=50, choices=categories)

    def __str__(self):
        return str(self.category)


class SubCategoryList(models.Model):
    category = models.ForeignKey(CategoryList)
    subcategory = models.CharField(max_length=50)

    def __str__(self):
        return str(self.subcategory)


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return str(self.city)


class OfferPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    subcategory = models.ForeignKey(SubCategoryList)
    city = models.ForeignKey(City)
    photo = models.ImageField(upload_to='post_photos', name='photo', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'


@receiver(post_save, sender='auth.user')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        UserProfile.objects.create(user=instance)
