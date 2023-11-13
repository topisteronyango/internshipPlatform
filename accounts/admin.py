from django.contrib import admin
from .models import Profile , City

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone_number', 'image']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']