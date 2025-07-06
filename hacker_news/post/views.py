from django.http import HttpResponseBadRequest
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import F
from .models import Post
from .forms import PostForm

# Create your views here.

# def index_view(request):
#     return HttpResponse("Hello, there!")

class PostsView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "post_list.html", context)  

# def posts_view(request):
    # if request.method == "GET":
        # posts = Post.objects.all()
        # result = ", ".join([p.title for p in posts])
        # context = {"posts": posts}
        # return HttpResponse(result)
        # return render(request, "post_list.html", context)  

    # elif request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data["title"]
    #         body = form.cleaned_data["body"]
    #         author_name = form.cleaned_data["author_name"]
            
    #         post = Post.objects.create(
    #             title=title, body=body, author_name=author_name
    #         )
    #         context = {"post": post, "form": PostForm}
    #         return render(request, "post_detail.html", context)
        # title = request.POST.get("title")
        # body = request.POST.get("body")
        # author_name = request.POST.get("author_name")

        # if not (type(title) is str and 0 < len(title) <= 128):
        #     return HttpResponseBadRequest("Invalid Title")
        # if not (type(body) is str and 0 < len(title) <= 1024):
        #     return HttpResponseBadRequest("Invalid Body")
        # if not (type(author_name) is str and 0 < len(title) <= 32):
        #     return HttpResponseBadRequest("Invalid author_name")
        
        # posts = Post.objects.all()
        # context = {"posts": posts, "form": form}
        # return render(request, "post_list.html", context)  
        # return redirect("posts")

class PostCreateView(View):
    def get(self, request):
        context = {"form": PostForm}
        return render(request, "post_create.html", context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            author_name = form.cleaned_data["author_name"]
            
            post = Post.objects.create(
                title=title, body=body, author_name=author_name
            )
            context = {"post": post}
            return render(
                request, "post_detail.html", context
            )
        return redirect("posts")


# def post_create_view(request):
#     if request.method == "GET":
#         context = {"form": PostForm}
#         return render(request, "post_create.html", context)
#     elif request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data["title"]
#             body = form.cleaned_data["body"]
#             author_name = form.cleaned_data["author_name"]
            
#             post = Post.objects.create(
#                 title=title, body=body, author_name=author_name
#             )
#             context = {"post": post}
#             return render(
#                 request, "post_detail.html", context
#             )
#         return redirect("posts")

class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        context = {"post": post}
        return render(request, "post_detail.html", context)    
    

# def post_view(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     context = {"post": post}
#     return render(request, "post_detail.html", context)

class PostLikeView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.points = F("points") + 1
        post.save()
        post.refresh_from_db()
        context = {"post": post} 
        return render(request, "post_detail.html", context)


# def post_like_view(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     post.points = F("points") + 1
#     post.save()
#     post.refresh_from_db()
#     context = {"post": post}
#     return render(request, "post_detail.html", context)

