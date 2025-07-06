from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from post import views

urlpatterns = [
    # path("index/", views.index_view, name="post_index")
    path("", views.posts_view, name="posts"),
    path("create/", views.post_create_view, name="post_create"),
    path("<int:post_id>", views.post_view, name="post"),
    path("<int:post_id>/like/", views.post_like_view, name="post_like"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)