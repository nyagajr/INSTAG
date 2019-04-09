from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    profile_name = models.CharField(max_length =30)

    # user_id = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    Bio = models.CharField(max_length =50)
    def __str__(self):
        return self.profile_name
