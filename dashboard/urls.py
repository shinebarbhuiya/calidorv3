from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('blog_topic/', views.blog_topic_generator, name='blog_topic_generator'),
    

 
]
