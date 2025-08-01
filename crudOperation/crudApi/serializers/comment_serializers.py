
from rest_framework import serializers
from crudApi.models.comment_models import Comments





class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id','blog_id','name','email','status','created_at']

    
    
            



