from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# from rest_framework import permissions
# from rest_framework import viewsets
# from .serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import SnippetSer
from .models import Snippet

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST'])
def home_list(request):
    if request.method=='GET':
        snippets=Snippet.objects.all()
        serializer=SnippetSer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=SnippetSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def getDetail(request, pk):

    try:
        snippets=Snippet.objects.get(id=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer=SnippetSer(snippets, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def post(request):
    if request.method=='POST':
        serializer=SnippetSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })








# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

