
from django.db import models

class Contact (models.Model):
    Full_Name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(blank=False)
    Company_name = models.CharField(max_length=30, blank=False)
    Country = models.CharField(max_length=30, blank=False)
    Phone_Number = models.CharField(max_length=20, blank=False)
    Message = models.TextField(blank=False)
    Creation_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_Name