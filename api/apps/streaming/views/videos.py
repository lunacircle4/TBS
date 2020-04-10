import logging
from .base import BaseViewSet
from ..mixins.videos import CreateModelMixin
from rest_framework.response import Response

from ..models import Video 
from ..serializers.videos import (
    ListSerializer,
    DetailSerializer
)

class VideoViewset(BaseViewSet, CreateModelMixin):
    queryset = Video.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListSerializer
        else:
            return DetailSerializer

##
# video를 올리면
# 섬네일을 생성하고
# 저장시 같이 저장한다.