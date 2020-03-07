from django.db import models
from django.contrib.auth.models import User
import uuid
import os


"""
------------------------------------------
Method to provide filename and upload path
------------------------------------------
"""
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/photos', filename)


"""
Model to manage photo gallery
"""
class Gallery(models.Model):

    photo = models.FileField(upload_to=get_file_path,)
    caption = models.CharField(
                        max_length=200,
                        null=True,
                        blank=True,
                    )
    user = models.ForeignKey(
                        User, on_delete=models.CASCADE,
                        related_name='photos',
                        null=True,
                        blank=True,
                    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'photos'
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-updated_at']

    def __str__(self):
        return "Uploaded on : " + str(self.created_at)
