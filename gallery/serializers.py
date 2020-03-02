from rest_framework import serializers
from .models import Gallery

class PhotosSerializer(serializers.Serializer):
    photo = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    class Meta:
        model = Gallery
        fields = ('photo', 'created_at', 'updated_at')
