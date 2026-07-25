from django.shortcuts import render
from .models import Post, Service

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    services = Service.objects.all().order_by('order')
    
    # for post in posts:
    #     print(f"Post ID: {post.id}")
    #     print(f"Username: {post.username}")
    #     print(f"Caption: '{post.caption}'")
    #     print(f"Caption Type: {type(post.caption)}")
    #     print(f"Is Empty: {not post.caption}")
    #     print("-" * 50)
        
    return render(request, 'core/index.html', {
        'posts': posts,
        'services': services
    })