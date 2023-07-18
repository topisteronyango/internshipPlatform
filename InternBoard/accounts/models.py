from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# django signals
from django.db.models.signals import post_save 
from django.dispatch import receiver

# Create your models here.
# because django already includes user table in the database i have 2 choices to create a user 1. abstract a new user 2. extend from the existing one
class Profile(models.Model):
    # Relation One to One
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE , blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    image  = models.ImageField(upload_to='profile/')

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user)

class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name
    
    
# create new user ---> create new empty profile
# using signals in django: https://docs.djangoproject.com/en/4.1/topics/signals/

# django signals code from here: https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: # 201
        Profile.objects.create(user=instance)