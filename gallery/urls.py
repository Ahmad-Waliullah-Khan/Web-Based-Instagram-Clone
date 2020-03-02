from django.urls import path

from .views import PhotoList, PhotosUpload

app_name = 'api'
urlpatterns = [
    path('', PhotoList.as_view(), name='photos'),
    path('upload/', PhotosUpload.as_view(), name='upload-photos'),
]
