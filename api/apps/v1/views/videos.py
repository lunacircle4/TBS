import logging
from apps.v1.views.base import BaseViewSet
from rest_framework.response import Response

from apps.db.video.models import Video 
from apps.v1.serializers.videos import (
    ListSerializer,
    DetailSerializer
)

class VideoViewset(BaseViewSet):
    queryset = Video.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListSerializer
        else:
            return DetailSerializer
