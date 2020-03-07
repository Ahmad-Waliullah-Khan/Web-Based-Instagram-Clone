from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import magic

from .models import Gallery

def upload_photo(request):
    if request.method == 'POST':
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):

                    if is_valid_mime(formfile):
                        gallery = Gallery(caption=formfile, photo=formfile)
                        try:
                            gallery.save()
                            return JsonResponse('Photo(s) uploaded successfully!', safe=False)
                        except:
                            return JsonResponse('Error uploading photo', safe=False)
                    else:
                        return JsonResponse('File must be a png or jpeg image.', safe=False)

def is_valid_mime(in_memory_file):
    mime = magic.from_buffer(in_memory_file.read(), mime=True)
    if mime == 'image/jpeg' or mime == 'image/png':
        return True
    return False
