from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def getAllPosts(request):
    posts = Post.objects.all()
    data = PostSerializer(posts, many=True)
    return Response(data.data)


@api_view(['GET'])
def getSinglePost(request, pk):
    posts = Post.objects.get(id=pk)
    data = PostSerializer(posts)
    return Response(data.data)


@api_view(['POST'])
def addPost(request):
    data = PostSerializer(data=request.data)
    if data.is_valid():
        data.save()
    return Response(data.data)


@api_view(['GET'])
def deletePost(request, pk):
    data = Post.objects.get(id=pk)
    tmpData = data
    data.delete()
    return Response(tmpData.data)
