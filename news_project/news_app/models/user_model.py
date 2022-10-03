from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from news_app.managers import UserManager

class User(AbstractBaseUser):
    username        = models.CharField(max_length=30, unique=True)
    email           = models.EmailField(max_length=60, unique=True)
    is_staff        = models.BooleanField(default=False)
    profile_image   = models.ImageField(max_length=255, 
                                        upload_to='profile_images', 
                                        default='default_profile_image.png', 
                                        null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username