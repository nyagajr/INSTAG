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

    @classmethod
    def search_by_profile_name(cls,search_term):
        app = Profile.objects.filter(profile_name__icontains=search_term)
        return app


class Comments(models.Model):
    comment = models.CharField(max_length =30)

    def __str__(self):
        return self.comment

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    image_profile = models.ForeignKey(Profile)
    img_comments = models.ForeignKey(Comments)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.image_name
