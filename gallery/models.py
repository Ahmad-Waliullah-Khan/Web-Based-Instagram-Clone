from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField

from .utility_methods import get_file_path


#===============================================================================
# Model to manange Gallery data
#===============================================================================
class Gallery(models.Model):

    photo_size_240 = ResizedImageField(size=[240, 135],
                            upload_to=get_file_path,null=True,
                            blank=True,
                        )
    photo_size_720 = ResizedImageField(size=[720, 405],
                            upload_to=get_file_path,null=True,
                            blank=True,
                        )
    photo = ResizedImageField(size=[1200, 675], upload_to=get_file_path,)
    caption = models.CharField(
                        max_length=200,
                        null=True,
                        blank=True,
                    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
                        User, on_delete=models.CASCADE,
                        related_name='photos',
                        null=True,
                        blank=True,
                    )
    
    #===========================================================================
    # __str__
    #===========================================================================
    def __str__(self):
        return str(self.caption)+ " | Uploaded on : " + str(self.created_at)

    
    #===========================================================================
    # Meta
    #===========================================================================
    class Meta:
        db_table = 'photos'
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-created_at']
