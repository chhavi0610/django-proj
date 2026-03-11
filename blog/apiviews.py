from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache

@api_view(['GET'])
def get_posts(request):
     cached_posts = cache.get("posts")

     if cached_posts:
          return Response(cached_posts)
     
     posts = Post.objects.all()
     serializer = PostSerializer(posts, many = True)
     cache.set("posts", serializer.data, timeout=60)


     return Response(serializer.data)

@api_view(["GET"])
def get_post(resquest, id):

     post = Post.objects.get(id = id)
     serializer = PostSerializer(post, many=False)

     

     return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request):
     
    serializer = PostSerializer(data = request.data)

    if serializer.is_valid():
         serializer.save()
         cache.delete("posts")
         return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_post(request, id):
     
     post = Post.objects.get(id = id)
     post.delete()

     return Response({"message":"post deleted"})