from rest_framework.views import APIView

from .serializers import PhotosSerializer
from .models import Gallery


class PhotoList(APIView):
    def get(self, request, format=None):
        serializer = PhotosSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response({serializer.data}, status=status.HTTP_200_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotosUpload(APIView):
    def post(self, request, format=None):
        serializer = PhotosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
