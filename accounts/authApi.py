from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegistrationSerializer, LoginSerializer, ProfileSerializer
from knox.views import LoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action, api_view

# RegistrationAPI
class RegistrationAPI(generics.GenericAPIView):
    '''
    This class will register a new user once the registration endpoint is called
    '''
    serializer_class=RegistrationSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })


# LoginAPI
class LoginAPI(generics.GenericAPIView):
    '''
    This class will authenticate a user once the login endpoint is called
    '''
    serializer_class=LoginSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=(permissions.AllowAny,)

    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]   
        })


# UserAPI
class UserAPI(generics.RetrieveAPIView):
    '''
    This class will return user details when the user endpoint is called
    '''
    permission_classes=[
        permissions.IsAuthenticated,
    ]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user


# ProfileAPI
class ProfileAPI(generics.GenericAPIView):
    '''
    This class will return user details when the user endpoint is called
    '''
    permission_classes=[
        permissions.IsAuthenticated,
    ]
    serializer_class=ProfileSerializer
    def get_object(self):
        return self.request.profile

# Update Profile
@api_view(['GET','PUT','DELETE'])
def updateProfile(request,username):
    try:
        profile = Profile.objects.get(user__username=username)

    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializer
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, satus = HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

