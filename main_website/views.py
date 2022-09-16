from django.shortcuts import render, HttpResponse, Http404
from .models import *

icons = {"Discord": "https://discord.gg/KUjVAe4r",
         "YouTube": "https://www.youtube.com/channel/UCl65hO2BOoPA7c5QXiBV8VA",
         "TikTok":  "https://www.tiktok.com/@s5_university"}
icons_about = { "Telegram": "https://t.me/Delnold",
                "Gmail": "mailto:dmitrii.palienko@gmail.com",
                "Github": "https://github.com/Delnold"
}
def index(request):
    return render(request, 'index.html', {"icons": icons})
def about(request):
    return render(request, 'About.html', {"icons": icons, "icons_about": icons_about})

def docs(request):
    icons_champ = Champion.objects.all()
    return render(request,'Docs.html', {"icons": icons, 'icons_champ': icons_champ})
def test(request, slug):
    try:
        icons_champ = Champion.objects.get(champion_name = slug)
    except Champion.DoesNotExist:
        raise Http404
    return render(request,'Champion_page.html', {"icons": icons, 'icons_champ': icons_champ, 'slug': slug})

# Create your views here.