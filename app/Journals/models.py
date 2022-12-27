from django.db import models



class Journals (models.Model):
    articleTitle = models.CharField(max_length=50, blank=False)
    journalName = models.CharField(max_length=50, blank=False)
    journalLink = models.FileField(upload_to='ArticlePress/', blank=False)
    creationTime = models.DateTimeField(auto_now_add=True)
