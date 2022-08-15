from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


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

@api_view(['PUT'])
def updatePost(request, pk):
    instancePost = Post.objects.get(id=pk)
    data = PostSerializer(instance=instancePost, data=request.data)
    if data.is_valid():
        data.save()
    return Response(data.data)

@api_view(['DELETE'])
def deletePost(request, pk):
    data = Post.objects.get(id=pk)
    tmpData = data
    data.delete()
    return Response(tmpData.data)



@api_view(['GET'])
def getAllComments(request):
    comments = Comment.objects.all()
    data = CommentSerializer(comments, many=True)
    return Response(data.data)


@api_view(['GET'])
def getSingleComment(request, pk):
    comments = Comment.objects.get(id=pk)
    data = CommentSerializer(comments)
    return Response(data.data)


@api_view(['POST'])
def addComment(request):
    data = CommentSerializer(data=request.data)
    if data.is_valid():
        data.save()
    return Response(data.data)

@api_view(['PUT'])
def updateComment(request, pk):
    instanceComment = Comment.objects.get(id=pk)
    data = CommentSerializer(instance=instanceComment, data=request.data)
    if data.is_valid():
        data.save()
    return Response(data.data)

@api_view(['DELETE'])
def deleteComment(request, pk):
    data = Comment.objects.get(id=pk)
    data.delete()
    return Response()
