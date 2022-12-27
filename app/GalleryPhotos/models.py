from django.db import models


class Gallery (models.Model):
    categoryNameArab = models.CharField(max_length=50, blank=False)
    categoryNameFrench = models.CharField(max_length=50, blank=False)
    categoryNameEnglish = models.CharField(max_length=50, blank=False)
    creationTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryNameEnglish

class Images (models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='GalleryPhotos/', blank=False)
    creationTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery.categoryNameEnglish
        return f"imageCategory={self.gallery.categoryNameEnglish}|image={self.image}"