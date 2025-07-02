from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

# def index_view(request):
#     return HttpResponse("Hello, there!")

def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        # result = ", ".join([p.title for p in posts])
        context = {"posts": posts}
        # return HttpResponse(result)
        return render(request, "post_list.html", context)  

    elif request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        author_name = request.POST.get("author_name")

        if not (type(title) is str and 0 < len(title) <= 128):
            return HttpResponseBadRequest("Invalid Title")
        if not (type(body) is str and 0 < len(title) <= 1024):
            return HttpResponseBadRequest("Invalid Body")
        if not (type(author_name) is str and 0 < len(title) <= 32):
            return HttpResponseBadRequest("Invalid author_name")
        
        post = Post.objects.create(title=title, body=body, author_name=author_name)
        context = {"post": post}
        return render(request, "post_detail.html", context)




def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "post_detail.html", context)  