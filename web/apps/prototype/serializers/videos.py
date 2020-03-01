from rest_framework import serializers
from apps.tbs_core_db.models import Video

class ListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="prototype:video-detail")
    class Meta:
        model = Video
        fields = ['id', 'url']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_url']
    