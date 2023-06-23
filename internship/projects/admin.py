from django.contrib import admin

# Register your models here.
from .models import Specialization, Internship, Project
@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ProjectInline(admin.StackedInline):
    model = Project

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['title', 'internship', 'created']
    list_filter = ['created', 'internship']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectInline]