from django.db import models

class Video (models.Model):
    description = models.CharField(max_length=200, blank=False)
    videosLink = models.FileField(upload_to='Videos/', blank=False)
    creationTime = models.DateTimeField(auto_now_add=True)
