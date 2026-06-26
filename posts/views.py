from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "posts/index.html", {"posts": posts})
