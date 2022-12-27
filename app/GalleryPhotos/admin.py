from django.contrib import admin
from .models import Gallery, Images
# Register your models here.
admin.site.register([Gallery, Images])