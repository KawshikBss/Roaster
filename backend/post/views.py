from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getAllPosts(request):
    return Response({'post': 'post'})


@api_view(['GET'])
def getSinglePost(request, pk):
    return Response({'post': 'post' + pk})


@api_view(['POST'])
def addPost(request):
    return Response({'post': 'save post'})


@api_view(['GET'])
def deletePost(request, pk):
    return Response({'post': 'delete post' + pk})
