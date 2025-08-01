
from rest_framework import serializers
from crudApi.models.blog_models import Blogs
from crudApi.serializers.comment_serializers import CommentSerializer

class BlogsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Blogs
        fields = ['id','name', 'description', 'sort_description', 'image_name', 'status', 'created_at', 'updated_at','comments']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.context.get('hide_description'):
            data.pop('description', None)
        return data
    

    # def create(self, validated_data):
    #     blog = Blogs.objects.create(
    #         name = validated_data['name'],
    #         description = validated_data['description'],
    #         sort_description = validated_data['sort_description'],
    #         image_name = validated_data['image_name'],
    #     )
    #     return blog
    
    
            



