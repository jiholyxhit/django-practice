from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from user.forms import CustomUserCreationForm
from django.config import settings

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
    

class SignUpView(View):
    def get(self, request):
        return render(
            request, "registration/sign_up.html",
            {"form": CustomUserCreationForm}
        )
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

class KakaoSocialLoginView(View):
    def get(self, request):
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize"
            f"?client_id={settings.KAKAO_REST_API_KEY}"
            f"&redirect_uri={settings.KAKAO_CALLBACK_URL}"
            f"&response_type=code"
        )
    

