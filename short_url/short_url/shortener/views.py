from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from shortener.models import ShortURL
from shortener.forms import ShortURLForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        short_urls = ShortURL.objects.all()
        context = {"short_urls": short_urls, "form": ShortURLForm}
        return render(request, "home.html", context)
    
class ShortURLCreateView(View):
    def post(self, request):
        form = ShortURLForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
        
        #check duplicates
        while True:
            code = ShortURL.generate_code()
            if not ShortURL.objects.filter(code=code).exists():
                break

        obj.code = code
        obj.save()
        return redirect("home")