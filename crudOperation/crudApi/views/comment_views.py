from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from crudApi.serializers import CommentSerializer
from crudApi.models.comment_models import Comments
from django.shortcuts import get_object_or_404
# Create your views here.



class Commentsview(APIView):

        def get(self, request, id = None):
                if id:
                        Comment = get_object_or_404(Comments,id=id)
                        serializer = CommentSerializer(Comment)
                        return Response(serializer.data)
                else:
                        comment = Comments.objects.all()
                        serializer  = CommentSerializer(comment, many = True)
                        return Response(serializer.data)


        def post(self, request):
                data = request.data
                serializer = CommentSerializer(data = data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
        

        def patch(self, request, id):
                data = request.data
                comment = get_object_or_404(Comments, id=id)
                serializer = CommentSerializer(comment, data=data, partial = True)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)


        def delete(self, request, id):
                comment = get_object_or_404(Comments, id = id)
                comment.delete()
                return Response({"message":f"Id {id} deleted successfully"})
