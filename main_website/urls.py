from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('docs/', views.docs, name = 'docs'),
    path('champion/<str:slug>/', views.test, name = 'champion')
]