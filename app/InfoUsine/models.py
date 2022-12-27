from django.db import models



class InfoUsine (models.Model):
    infoUsineArLink = models.FileField(upload_to='InfoUsine/Ar/', blank=False)
    infoUsineFrLink = models.FileField(upload_to='InfoUsine/Fr/', blank=False)
    creationTime = models.DateTimeField(auto_now_add=True)
