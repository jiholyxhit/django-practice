# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

# def index_view(request):
#     return HttpResponse("Hello, there!")

def posts_view(request):
    posts = Post.objects.all()
    # result = ", ".join([p.title for p in posts])
    context = {"posts": posts}
    # return HttpResponse(result)
    return render(request, "post_list.html", context)  

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "post_detail.html", context)  