from django.db import models
from apps.db.interface import Timestamp

class Video(Timestamp):
    video = models.FileField(upload_to="user_videos/", max_length=100)
    class Meta:
        db_table = "video"
