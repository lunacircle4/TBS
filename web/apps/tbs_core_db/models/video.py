from django.db import models
from .timestamp import TimeStamp

class Video(TimeStamp):
    video_url = models.FileField(upload_to="user_videos/", max_length=100)