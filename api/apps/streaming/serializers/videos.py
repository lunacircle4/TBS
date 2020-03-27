from rest_framework import serializers
from ..models import Video

class ListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="streaming:video-detail")
    class Meta:
        model = Video
        fields = ['id', 'url']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video']