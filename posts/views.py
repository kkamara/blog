from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "posts/index.html", {"posts": posts})

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post.html", {"post": post})
