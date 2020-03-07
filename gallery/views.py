from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import Gallery

def upload_photo(request):
    if request.method == 'POST':
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    gallery = Gallery(caption=formfile, photo=formfile)
                    try:
                        gallery.save()
                        return JsonResponse('Photo(s) uploaded successfully!', safe=False)
                    except:
                        return JsonResponse('Error uploading photo', safe=False)
