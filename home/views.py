from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from gallery.models import Gallery

from .forms import LoginForm


#===============================================================================
# home
#===============================================================================
@login_required(login_url='/')
def home(request):
    photos_list = Gallery.objects.order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(photos_list, 30) #loads 30 images per page
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


#===============================================================================
# upload
#===============================================================================
@login_required(login_url='/')
def upload(request):

    return render(
        request, 'home/upload.html',
        {}
    )


#===============================================================================
# index
#===============================================================================
def index(request):
    
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:gallery'))
    elif request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home:gallery'))
    return render(request, 'home/login.html', {'login_form': form })

#===============================================================================
# user_logout
#===============================================================================
@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:user_login'))
