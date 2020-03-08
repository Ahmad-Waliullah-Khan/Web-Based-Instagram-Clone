from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from gallery.models import Gallery

"""
--------------------------------------------------------------------------------
View for loading the gallery
--------------------------------------------------------------------------------
"""
@login_required(login_url='/')
def home(request):
    photos_list = Gallery.objects.order_by('-created_at')

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
@login_required(login_url='/')
def upload(request):

    return render(
        request, 'home/upload.html',
        {}
    )

"""
--------------------------------------------------------------------------------
Index
--------------------------------------------------------------------------------
"""
def index(request):
    if not request.user.is_authenticated:
        return render(
            request, 'home/index.html',
        )
    else:
        return HttpResponseRedirect(reverse('home:gallery'))

"""
--------------------------------------------------------------------------------
Login
--------------------------------------------------------------------------------
"""
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home:gallery'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, '')

"""
--------------------------------------------------------------------------------
Logout
--------------------------------------------------------------------------------
"""
@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))
