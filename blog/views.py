from django.shortcuts import render
from posts.models import Post

def index(request):
    posts = Post.objects.all().filter(published=True)
    return render(request, "index", { "posts": posts })
