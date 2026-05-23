from django.shortcuts import render
from .models import Post, Service

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    services = Service.objects.all().order_by('order')
    return render(request, 'core/index.html', {
        'posts': posts,
        'services': services
    })