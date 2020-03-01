from apps.prototype.views.base import BaseViewSet
from rest_framework.response import Response

from apps.tbs_core_db.models.video import Video 
from apps.prototype.serializers.videos import (
    ListSerializer,
    DetailSerializer
)

class VideoViewset(BaseViewSet):
    queryset = Video.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return ListSerializer
        else:
            return DetailSerializer