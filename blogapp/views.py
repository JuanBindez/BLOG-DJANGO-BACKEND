import re
from django.shortcuts import render
from .models import Post


# Create your views here.
def hello_home(request):
    return render(request, 'index.html')

def hello_blog(request):
    list_posts = Post.objects.all()
    data = {'posts': list_posts }
    return render(request, 'blog.html', data)
