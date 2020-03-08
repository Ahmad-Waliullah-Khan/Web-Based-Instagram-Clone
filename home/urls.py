from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('gallery', views.home, name='gallery'),
    path('upload/', views.upload, name='upload'),
]
