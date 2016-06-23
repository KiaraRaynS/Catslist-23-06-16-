from django.contrib import admin
from appcatslist.models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(UserProfile, UserProfileAdmin)
