from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().filter(status=Post.Status.PUBLISHED)
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Publish'

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
            ]



    def __str__(self):
        return self.title