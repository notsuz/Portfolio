from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Post(models.Model):
    # User Info
    username = models.CharField(max_length=100, default="quietlyodd")
    profile_pic = CloudinaryField('image', folder='profile_pics/', blank=True, null=True)
    
    # Post Content
    main_post_img = CloudinaryField('image', folder='post_images/',blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    
    # Stats & Metadata
    likes_text = models.CharField(max_length=100, default="Liked by 210 others", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.created_at.strftime('%Y-%m-%d')}"
    
    
class Service(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title