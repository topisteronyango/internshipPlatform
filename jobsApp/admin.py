from django.contrib import admin
from .models import Job, Category, Apply

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'vacancy', 'salary', 'experience', 'category']
    list_filter = ['job_type', 'experience', 'salary']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class ApplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'cv', 'created_at']

admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Apply, ApplyAdmin)
