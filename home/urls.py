from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('upload/', views.upload, name='upload'),
]
