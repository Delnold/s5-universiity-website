from django.shortcuts import render, HttpResponse, Http404, redirect
from main_website.models import *
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

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
    champions = Champions.objects.all()
    return render(request, 'Docs.html', {"icons": icons, "icons_about": icons_about, "champions": champions})
# Create your views here.
def champion_page(request, champ):
    try:
        champions = Champions.objects.get(champion_name=champ)
        skills = champions.championsskills_set.all()
        runes = champions.runes_set.all()
        champ_exists = request.user.champions_set.contains(champions)
    except Champions.DoesNotExist:
        raise Http404
    return render(request, 'Champion_page.html', {"icons": icons, 'champions': champions, 'champ': champ, 'skills': skills, 'champ_exists': champ_exists})
def register_form(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        return render(request, 'Login.html', {"icons": icons, "icons_about": icons_about, "login_form": form})
    form = NewUserForm()
    return render(request, 'Register.html', {"icons": icons, "icons_about": icons_about, "register_form" : form})
def login_form(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        return render(request, 'Login.html', {"icons": icons, "icons_about": icons_about, "login_form": form})
    form = AuthenticationForm()
    return render(request, 'Login.html', {"icons": icons, "icons_about": icons_about, "login_form":form})

def logout_form(request):
    logout(request)
    return redirect('index')

def account_page(request):
    favourite_champions = request.user.champions_set.all()
    return render(request, 'UserPage.html', {"icons": icons, "favourite_champions": favourite_champions})

def favourite_champ_add_delete(request, champ):
    champions = Champions.objects.get(champion_name=champ)
    if request.POST.get('Addbtn'):
            request.user.champions_set.add(champions)
            return redirect('champion', champ=champ)
    if request.POST.get('Deletebtn'):
            request.user.champions_set.remove(champions)
            return redirect('champion', champ=champ)