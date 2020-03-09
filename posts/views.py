from django.shortcuts import render
from posts.models import Post

# Create your views here.
def get_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "post.html", {"post": post})
