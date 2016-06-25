from django.contrib import admin
from appcatslist.models import UserProfile, OfferPost, CategoryList, City, SubCategoryList

# Register your models here.


class OfferPostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'city']

admin.site.register(OfferPost, OfferPostAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferredcity']

admin.site.register(UserProfile, UserProfileAdmin)


class CategoryListAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(CategoryList, CategoryListAdmin)


class SubCategoryListAdmin(admin.ModelAdmin):
    list_display = ['subcategory']

admin.site.register(SubCategoryList, SubCategoryListAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

admin.site.register(City, CityAdmin)
