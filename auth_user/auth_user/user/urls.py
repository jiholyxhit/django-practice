from django.urls import path, include
from user import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("users/", include("django.contrib.auth.urls")),
    path("users/sing-up/", views.SignUpView.as_view(), name="sign_up"),
    path("useres/social/kakao/login/", views.KakaoSocialLoginView.as_view(), name="kakao_social_login")
]

