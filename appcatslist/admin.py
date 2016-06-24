from django.contrib import admin
from appcatslist.models import UserProfile, OfferPost, CategoryList, City

# Register your models here.


class OfferPostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price']

admin.site.register(OfferPost, OfferPostAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferredcity']

admin.site.register(UserProfile, UserProfileAdmin)


class CategoryListAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(CategoryList, CategoryListAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

admin.site.register(City, CityAdmin)
