import requests, uuid

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import login
# from django.contrib.auth.models import User
from user.models import CustomUser
from user.forms import CustomUserCreationForm
from django.conf import settings

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


class KakaoCallbackView(View):
    def get(self, request):
        auth_code = request.GET.get("code")

        #Kakao에 auth_code를 통해서 access_token 요청하고 응답받기
        response = requests.post(
            "https://kauth.kakao.com/oauth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
            data = {
                "grant_type": "authorization_code",
                "client_id": settings.KAKAO_REST_API_KEY,
                "redirect_uri": settings.KAKAO_CALLBACK_URL,
                "code": auth_code,
            }
        )

        if response.ok:
            access_token = response.json().get("access_token")

            #Kakao user profile query with access_token
            profile_response = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    # "Content-Type": "Content-Type: application/x-www-form-urlencoded;charset=utf-8"
                }
            )

            if profile_response.ok:

                username = f"K#{profile_response.json()["id"]}"
                email = profile_response.json()["kakao_account"]["email"]


                try:
                    #checking if the user already have existed
                    user = CustomUser.objects.get(username=username)
                except CustomUser.DoesNotExist:
                    user = CustomUser.objects.create_user(
                        username = username,
                        email = email,
                        password = str(uuid.uuid4()),
                        social_provider = "kakao",
                    )
                
                #Session Login (django.contrib.auth 'login' module)
                login(request, user)
                return redirect("home")
            
        return JsonResponse({"error": "Social Login Failed."})
                 
            
        
    

