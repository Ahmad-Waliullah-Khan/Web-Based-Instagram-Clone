from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gallery.models import Gallery

"""
--------------------------------------------------------------------------------
View for loading the gallery
--------------------------------------------------------------------------------
"""
def home(request):
    photos_list = Gallery.objects.all()
    print('loaded photos : ', photos_list )

    page = request.GET.get('page', 1)
    paginator = Paginator(photos_list, 3) #loads 30 images per page
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)


    return render(
        request, 'home/gallery.html',
        {'photos' : photos,}
    )

"""
--------------------------------------------------------------------------------
View for uploading photo
--------------------------------------------------------------------------------
"""
def upload(request):

    return render(
        request, 'home/upload.html',
        {}
    )
