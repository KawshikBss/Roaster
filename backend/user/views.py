from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer
from .models import Profile


@api_view(['GET'])
def getAllUsers(request):
    profiles = Profile.objects.all()
    data = ProfileSerializer(profiles, many=True)
    return Response(data.data)

@api_view(['GET'])
def getSingleUser(request, pk):
    profile = Profile.objects.get(id=pk)
    data = ProfileSerializer(profile, many=False)
    return Response(data.data)

@api_view(['POST'])
def addUser(request):
    data = ProfileSerializer(data=request.data)
    if data.is_valid():
        data.save()
    return Response(data.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return Response()
