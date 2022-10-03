from django.db import models
from .user_model import User
from .tag_model import Tag 

class Post(models.Model):
    title           = models.CharField(max_length=30)
    content         = models.TextField(max_length=300)
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags            = models.ManyToManyField(Tag, related_name="posts")
    picture         = models.ImageField(max_length=255, 
                                        upload_to='post_images', 
                                        default='default_post_image.png', 
                                        null=True, blank=True)

    def __str__(self):
        return self.title