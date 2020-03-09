from django.http import JsonResponse
import magic

from .models import Gallery


#===============================================================================
# upload_photo
#===============================================================================
def upload_photo(request):
    """
    View method to upload photo
    """
    if request.method == 'POST':
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):

                    # check for image type
                    if is_valid_mime(formfile):

                        # resize and save image
                        try:
                            gallery = Gallery(
                                caption=formfile,
                                photo=formfile,
                                photo_size_240=formfile,
                                photo_size_720=formfile,
                                user=request.user,
                            )
                            gallery.save()
                        except:
                            return JsonResponse(
                                'Error uploading photo.', safe=False, status=400
                            )
                        return JsonResponse(
                                'Photo(s) uploaded successfully!', safe=False,
                                status=200
                            )
                    else:
                        return JsonResponse(
                            'File must be a png or jpeg image.',
                            safe=False, status=400
                        )

#===============================================================================
# is_valid_mime
#===============================================================================
def is_valid_mime(in_memory_file):
    """
    Checks file type for png or jpeg and returns True or False
    """

    mime = magic.from_buffer(in_memory_file.read(), mime=True)
    if mime == 'image/jpeg' or mime == 'image/png':
        return True
    return False
