from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # Link UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __unicode__(self):
        return self.user.username
