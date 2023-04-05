from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse, Http404, redirect
from main_website.models import *
from .forms import NewUserForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from main_website.statistics import generate_chart_favourite_champion, generate_chart_videos_champion
from main_website.excel_files import excel_view, excel_admin_upload
from main_website.additional_decorators import staff_required
import base64

def index(request):
    return render(request, 'index.html')

def docs(request):
    champions = Champions.objects.all()
    return render(request, 'Docs.html', {"champions": champions})
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
    return render(request, 'Champion_page.html', {'champions': champions, 'champ': champ, 'skills': skills, 'champ_exists': champ_exists})
def register_form(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        return render(request, 'Login.html', {"login_form": form})
    form = NewUserForm()
    return render(request, 'Register.html', {"register_form" : form})
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
        return render(request, 'Login.html', { "login_form": form})
    form = AuthenticationForm()
    return render(request, 'Login.html', {"login_form":form})

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
                              { "favourite_champions": favourite_champions, "user_check": user_check,"profile_form": form})
        form = ProfileForm()
        return render(request, 'UserPage.html', { "favourite_champions": favourite_champions, "user_check": user_check, "profile_form": form})
    else:
        return render(request, 'UserPage.html', {"favourite_champions": favourite_champions, "user_check": user_check})
@login_required
def favourite_champ_add_delete(request, champ):
    champions = Champions.objects.get(champion_name=champ)
    if request.POST.get('Addbtn'):
            request.user.champions_set.add(champions)
            return redirect('champion', champ=champ)
    if request.POST.get('Deletebtn'):
            request.user.champions_set.remove(champions)
            return redirect('champion', champ=champ)
def chall_videos(request: WSGIRequest)-> HttpResponse:
    chall_videos = ChallVideos.objects.all()
    return render(request, 'ChallVideos.html', {"chall_videos": chall_videos})

def champion_favorites(request):
    dict_favourites_champions = {"champions": [], "count":[]}
    dict_videos_champions = {"champions": [], "videos_count": []}

    favourites_champ = Champions.users_favourite.through.objects
    videos = ChallVideos.objects.all()
    all_champions_users_favourite = list(Champions.objects.filter(users_favourite__champions__isnull=False).distinct())

    for i in videos:
            champ_count = videos.filter(champion_id=i.champion_id).count()
            champ_name = Champions.objects.get(champion_id=i.champion_id).champion_name
            if champ_name not in dict_videos_champions["champions"]:
                dict_videos_champions["champions"].append(champ_name)
                dict_videos_champions["videos_count"].append(champ_count)

    for i in all_champions_users_favourite:
        champ_count = favourites_champ.filter(champions_id = i.champion_id).count()
        dict_favourites_champions["champions"].append(i)
        dict_favourites_champions["count"].append(champ_count)
    chart_favourite = generate_chart_favourite_champion(dict_favourites_champions).content
    chart_favourite = base64.b64encode(chart_favourite).decode('utf-8')

    chart_videos_champ = generate_chart_videos_champion(dict_videos_champions).content
    chart_videos_champ = base64.b64encode(chart_videos_champ).decode('utf-8')
    return render(request, 'Statistics.html', {'chart_favourite': chart_favourite, 'chart_videos': chart_videos_champ})


def champions_to_excel(request: WSGIRequest)->HttpResponse:
    champions = Champions.objects.all()
    excel_file = excel_view(request, champions)
    return excel_file


@staff_required
def excel_to_champions(request: WSGIRequest):
   if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        if excel_admin_upload(excel_file) == False:
            return render(request, '400.html')
   return redirect('docs')
