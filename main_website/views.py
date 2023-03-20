from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, Http404, redirect
from main_website.models import *
from .forms import NewUserForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from main_website.statistics import generate_chart_favourite_champion
import base64

icons = {"Discord": "https://discord.gg/KUjVAe4r",
         "YouTube": "https://www.youtube.com/channel/UCl65hO2BOoPA7c5QXiBV8VA",
         "TikTok":  "https://www.tiktok.com/@s5_university"}
icons_about = { "Telegram": "https://t.me/Delnold",
                "Gmail": "mailto:dmitrii.palienko@gmail.com",
                "Github": "https://github.com/Delnold"
}
def index(request):
    return render(request, 'index.html', {"icons": icons})

def docs(request):
    champions = Champions.objects.all()
    return render(request, 'Docs.html', {"icons": icons, "icons_about": icons_about, "champions": champions})
# Create your views here.
def champion_page(request, champ):
    try:
        champ_exists = False
        champions = Champions.objects.get(champion_name=champ)
        skills = champions.championsskills_set.all()
        runes = champions.runes_set.all()
        items = champions.items_set.all()
        if request.user.is_authenticated:
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

def account_page(request, username):
    user_check = User.objects.get(username=username)
    favourite_champions = user_check.champions_set.all()
    user_extended = None
    if request.user.username == username:
        if request.method == "POST":
            if UserExtended.objects.filter(username = user_check).exists():
                user_extended = UserExtended.objects.get(username = user_check)
            else:
                user_extended = UserExtended(username = user_check)

            form = ProfileForm(request.POST, request.FILES, instance=user_extended)
            if form.is_valid():
                form.save()
                return render(request, 'UserPage.html',
                              {"icons": icons, "favourite_champions": favourite_champions, "user_check": user_check,"profile_form": form})
        form = ProfileForm()
        return render(request, 'UserPage.html', {"icons": icons, "favourite_champions": favourite_champions, "user_check": user_check, "profile_form": form})
    else:
        return render(request, 'UserPage.html', {"icons": icons, "favourite_champions": favourite_champions, "user_check": user_check})
@login_required
def favourite_champ_add_delete(request, champ):
    champions = Champions.objects.get(champion_name=champ)
    if request.POST.get('Addbtn'):
            request.user.champions_set.add(champions)
            return redirect('champion', champ=champ)
    if request.POST.get('Deletebtn'):
            request.user.champions_set.remove(champions)
            return redirect('champion', champ=champ)
def chall_videos(request):
    chall_videos = ChallVideos.objects.all()
    return render(request, 'ChallVideos.html', {"icons": icons, "chall_videos": chall_videos})

def champion_favorites(request):
    dict_favourites = {"champions": [], "count":[]}
    favourites = Champions.users_favourite.through.objects
    all_champions = list(Champions.objects.filter(users_favourite__champions__isnull=False).distinct())
    for i in all_champions:
        champ_count = favourites.filter(champions_id = i).count()
        dict_favourites["champions"].append(i)
        dict_favourites["count"].append(champ_count)
    chart_favourite = generate_chart_favourite_champion(dict_favourites).content
    chart_favourite = base64.b64encode(chart_favourite).decode('utf-8')
    return render(request, 'Statistics.html', {'chart': chart_favourite, "icons": icons })