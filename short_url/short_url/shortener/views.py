from django.shortcuts import render
from django.views import View

from shortener.models import ShortURL

# Create your views here.

class HomeView(View):
    def get(self, request):
        short_urls = ShortURL.objects.all()
        return render(request, "home.html", {"short_urls": short_urls})