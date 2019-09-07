from django.shortcuts import render
from .models import Post
from django.utils import timezone


def new_post(request):
    posts = Post.objects.filter(active=True, published_date__lte=timezone.now())
    context={
        "posts":posts
        }
    return render(request, "posts.html", context)

