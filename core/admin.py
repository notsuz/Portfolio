from django.contrib import admin
from .models import Post, Service 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Change 'likes_count' to 'likes_text'
    list_display = ('username', 'likes_text', 'created_at') 
    search_fields = ('caption', 'username', 'background_title')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')