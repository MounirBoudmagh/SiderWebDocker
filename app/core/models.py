
from django.db import models

class Contact (models.Model):
    Full_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Company_name = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Phone_Number = models.CharField(max_length=20)
    Message = models.TextField()
    Creation_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_Name