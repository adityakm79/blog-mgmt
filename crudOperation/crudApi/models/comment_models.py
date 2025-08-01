from django.db import models
from crudApi.models.blog_models import Blogs
# Create your models here.

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blogs, related_name="comments", db_column='blog_id', on_delete=models.CASCADE)
    # blog_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"

