from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from ..services.thumbnail_extract_service import ThumbnailExtractService

class CreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_video = self.perform_create(serializer)
        thumbnail_extract_service = ThumbnailExtractService(new_video.video)
        new_video.thumbnail = thumbnail_extract_service.call
        # new_video.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
