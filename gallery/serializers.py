from rest_framework import serializers

from .models import Gallery

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = ('photo', 'created_at', 'updated_at',)
