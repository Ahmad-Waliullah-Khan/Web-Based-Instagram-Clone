from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import magic
from PIL import Image
from resizeimage import resizeimage
import os
from io import StringIO
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .utility_methods import get_file_path

from .models import Gallery


"""
View method to upload photo
"""
def upload_photo(request):
    if request.method == 'POST':
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):

                    # check for image type
                    if is_valid_mime(formfile):

                        gallery = Gallery(
                                caption=formfile,
                                photo=formfile,
                            )

                        # save original raw image temprarily
                        try:
                            gallery.save()
                        except:
                            return JsonResponse(
                                'Error uploading photo',
                                safe=False,
                                status=400
                            )

                        # resize the image keeping aspect ratio
                        try:
                            basewidth = 1200
                            img = Image.open(gallery.photo.path)
                            wpercent = (basewidth/float(img.size[0]))
                            hsize = int((float(img.size[1])*float(wpercent)))
                            img = img.resize((basewidth,hsize), Image.ANTIALIAS)

                            filename = get_file_path(gallery, gallery.photo.path)

                            # save the resized image temprarily
                            img.save('media/'+filename)

                            # update the database with new image path
                            Gallery.objects.filter(pk=gallery.id).update(
                                photo=filename
                            )

                        except:
                            return JsonResponse(
                                    'Error resizing photo',
                                    safe=False,
                                    status=400
                                )

                        # resize the image to shorter edge of 240px, keeping
                        # aspect ratio intact
                        try:
                            basewidth = 240
                            img = Image.open(gallery.photo.path)
                            wpercent = (basewidth/float(img.size[0]))
                            hsize = int((float(img.size[1])*float(wpercent)))
                            img = img.resize((basewidth,hsize), Image.ANTIALIAS)

                            filename = get_file_path(gallery, gallery.photo.path)

                            # save the resized image temprarily
                            img.save('media/'+filename)

                            # update the database with new image path
                            Gallery.objects.filter(pk=gallery.id).update(
                                photo_size_240=filename
                            )
                        except:
                            return JsonResponse(
                                    'Error resizing photo',
                                    safe=False,
                                    status=400
                                )

                        # resize the image to shorter edge of 720px, keeping
                        # aspect ratio intact
                        try:
                            basewidth = 720
                            img = Image.open(gallery.photo.path)
                            wpercent = (basewidth/float(img.size[0]))
                            hsize = int((float(img.size[1])*float(wpercent)))
                            img = img.resize((basewidth,hsize), Image.ANTIALIAS)

                            filename = get_file_path(gallery, gallery.photo.path)

                            # save the resized image temprarily
                            img.save('media/'+filename)

                            # update the database with new image path
                            Gallery.objects.filter(pk=gallery.id).update(
                                photo_size_720=filename
                            )
                        except:
                            return JsonResponse(
                                    'Error resizing photo',
                                    safe=False,
                                    status=400
                                )
                                
                        # remove tempoary resized image
                        os.remove(gallery.photo.path)

                        return JsonResponse('Photo(s) uploaded successfully!', safe=False, status=200)
                    else:
                        return JsonResponse('File must be a png or jpeg image.', safe=False, status=400)

"""
------------------------------------------
Method to checks for mime type
------------------------------------------
"""
def is_valid_mime(in_memory_file):
    """
    Checks file type for png or jpeg and returns True or False
    """

    mime = magic.from_buffer(in_memory_file.read(), mime=True)
    if mime == 'image/jpeg' or mime == 'image/png':
        return True
    return False
