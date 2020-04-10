from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from ..models import Video 

class Video(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_create(self):        
        testfile = SimpleUploadedFile(
            "videofile.mp4",
            b"videofiletest" 
        )
        response = self.client.post(
            '/videos', 
            {'video': testfile}
        )
        self.assertEqual(response.status_code, 201)
        
    def test_show(self):
        testfile = SimpleUploadedFile(
            "videofile.mp4",
            b"videofiletest" 
        )
        video = Video.objects.create(video=testfile)
        response = self.client.post(
            '/videos', 
            {'video': testfile}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['video'], '')

    def test_list(self):
        testfile = SimpleUploadedFile(
            "videofile.mp4",
            b"videofiletest" 
        )
        video = Video.objects.create(video=testfile)
        response = self.client.get('/videos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['video'], '')

    def test_update(self):
        testfile = SimpleUploadedFile(
            "videofile.mp4",
            b"videofiletest" 
        )
        updatedTestfile = SimpleUploadedFile(
            "videofile2.mp4",
            b"videofiletest" 
        )
        video = Video.objects.create(video=testfile)
        response = self.client.update(
            '/videos/{id}'.format(id=video.id), 
            {'video': updatedTestfile}
        )
        self.assertEqual(response.status_code, 205)
        self.assertEqual(response.data['video'], '')

    def test_delete(self):
        testfile = SimpleUploadedFile(
            "videofile.mp4",
            b"videofiletest" 
        )
        video = Video.objects.create(video=testfile)
        response = self.client.delete('/videos/{id}'.format(id=video.id))
        self.assertEqual(response.status_code, 204)
