#from django.db import modelsfrom pyexpat import model
from xml.dom import ValidationErr
import django
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django import forms
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user= models.IntegerField()
    bio= models.TextField(blank=True)
    profileimg= models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location= models.CharField(max_length= 100, blank=True)

    def __str__(self):
        return self.user.username

    def deleteimage(self):
        self.profile_images.delete()
        super().delete()

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    videos = models.FileField(upload_to='post_videos')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    def delete(self):
        self.videos.delete()
        super().delete()


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username