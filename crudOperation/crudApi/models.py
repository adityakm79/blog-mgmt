from django.db import models
import os
from datetime import datetime

# Create your models here.

def custom_image_upload_path(instance, filename):
    # Get extension
    ext = filename.split('.')[-1]
    # print(ext)
    name = instance.name.replace(" ", "_")
    # print(name)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{name}_{timestamp}.{ext}"
    return os.path.join('blogs', filename)



class Blogs(models.Model):
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sort_description = models.CharField(max_length=500)
    image_name = models.ImageField(upload_to=custom_image_upload_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        db_table = "blogs"





