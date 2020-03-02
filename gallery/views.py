from rest_framework import viewsets

from .serializers import GallerySerializer
from .models import Gallery


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-updated_at')
    serializer_class = GallerySerializer
