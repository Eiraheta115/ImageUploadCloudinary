from photoExample.models import photoExample
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import cloudinary, json
from photoExample.serializers import PhotoExampleSerializer

class photoExampleviewSet(viewsets.ModelViewSet):
    queryset = photoExample.objects.all()
    serializer_class = PhotoExampleSerializer

    @action(methods=['post'], detail=False)
    def uploadImage(self, request):
        data = json.loads(request.body)
        respon= cloudinary.uploader.upload(data["photo"])
        p = photoExample.objects.create(url=respon["url"])
        content = {'message': 'image uploaded and saved', 'photo': p.url}
        return Response(content, status=status.HTTP_201_CREATED)