from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('upload/', views.upload_photo, name='upload-photos'),
]
