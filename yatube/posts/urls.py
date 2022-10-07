# yatube/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/<slag:slag>/', views.group_posts),
] 