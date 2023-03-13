from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('champions/', views.docs, name = 'docs'),
    path('champions/<str:champ>/', views.champion_page, name = 'champion'),
    path('register/', views.register_form, name = 'register'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('account_page/', views.account_page, name='account_page'),
    path('champ_exists/<str:champ>/', views.favourite_champ_add_delete, name='champ_manipulation')
]