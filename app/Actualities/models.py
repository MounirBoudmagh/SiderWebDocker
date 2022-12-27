from django.db import models



class Actualitie (models.Model):
    titleArab = models.CharField(max_length=50, blank=False)
    titleFrench = models.CharField(max_length=50, blank=False)
    titleEnglish = models.CharField(max_length=50, blank=False)
    descriptionArab = models.TextField(blank=False)
    descriptionFrench = models.TextField(blank=False)
    descriptionEnglish = models.TextField(blank=False)
    imageLink = models.ImageField(upload_to='Actualities/images/', blank=True)
    isVideo = models.BooleanField(default=False)
    videoLink = models.FileField(upload_to='Actualities/videos', blank=True)
    Creation_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titleEnglish