from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudApi.serializers import BlogsSerializer
from crudApi.models.blog_models import Blogs
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

# Create your views here.




@api_view(["GET"])
def BlogGet(request):
        
        filters = Q()

        q = request.GET.get('q', '').strip()
        name = request.GET.get('name', '').strip()
        description = request.GET.get('description', '').strip()
        sort_description = request.GET.get('sort_description', '').strip()
        from_created_at = request.GET.get('from_created_at', '').strip()
        to_created_at = request.GET.get('to_created_at', '').strip()

        # print(q)
        # print('2324343546tgfgrey4u65i7iu6y5t44343546465786854545454448454512154')
        
        if q:
                filters &= (Q(name__icontains=q) | Q(sort_description__icontains=q) | Q(description__icontains=q))

        if name:
                filters &= Q(name__icontains=name)

        if description:
                filters &= Q(description__icontains=description)

        if sort_description:
                filters &= Q(sort_description__icontains=sort_description)
        
        if from_created_at:
                filters &= Q(created_at__date__gte=from_created_at)

        if to_created_at: 
                filters &= Q(created_at__date__lte=to_created_at)

        blogs = Blogs.objects.filter(filters)
        print(blogs.query)
      

        paginator = PageNumberPagination()
        paginator.page_size = 5  # or set from settings
        result_page = paginator.paginate_queryset(blogs, request)

        serializer = BlogsSerializer(result_page, many = True, context={'hide_description': True})
        return Response(serializer.data)



@api_view(["GET"])
def BlogGetById(request , id):
            blog = Blogs.objects.get(id = id)
        #     user.comments = Comments.objects.filter(Q(blog_id=id))
        #     print(blog)
            serializer = BlogsSerializer(blog)
            return Response(serializer.data)



@api_view(["POST"])
def BlogCreate(request):
        data = request.data
        # print(data)
        serializer = BlogsSerializer(data = data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["PUT"])
def BlogUpdate(request , id):
        blog = Blogs.objects.get(id = id)
        serializer = BlogsSerializer(blog , data = request.data, partial=True)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["DELETE"])
def BlogDelete(request, id):
        blog = Blogs.objects.get(id = id)
        blog.delete()
        return Response({"Message":f"Id {id} deleted successfully"})


@api_view(["PATCH"])
def BlogPatch(request, id):
        patch = Blogs.objects.get(id = id)
        serializer = BlogsSerializer(patch, data = request.data, partial = True)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)



