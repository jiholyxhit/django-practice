from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from post import views

urlpatterns = [
    # path("index/", views.index_view, name="post_index")
    path("", views.PostsView.as_view(), name="posts"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:post_id>", views.PostDetailView.as_view(), name="post"),
    path("<int:post_id>/like/", views.PostLikeView.as_view(), name="post_like"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)