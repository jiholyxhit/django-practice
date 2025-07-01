from django.http import HttpResponse
from .models import Post

# Create your views here.

# def index_view(request):
#     return HttpResponse("Hello, there!")

def posts_view(request):
    posts = Post.objects.all()
    result = ", ".join([p.title for p in posts])
    return HttpResponse(result)
    