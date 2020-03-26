from rest_framework import serializers
from apps.db.video.models import Video

class ListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="v1:video-detail")
    class Meta:
        model = Video
        fields = ['id', 'url']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video']
    