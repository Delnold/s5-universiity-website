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


# Create your views here.