from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegistrationSerializer, LoginSerializer
from knox.views import LoginView
from rest_framework.authentication import BasicAuthentication

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
class UserAPI(generics.GenericAPIView):
    '''
    This class will return user details when the user endpoint is called
    '''
    permission_classes=[
        permissions.IsAuthenticated,
    ]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user

