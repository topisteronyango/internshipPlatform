from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Internship(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class Specialization(models.Model):
    project_lead = models.ForeignKey(User,
    related_name='specializations_created',
    on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship,
    related_name='specializations',
    on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.title

class Project(models.Model):
    specialization = models.ForeignKey(Specialization,
    related_name='projects',
    on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title