from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile


# UserSerializer
class UserSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the User objects.
    '''
    class Meta:
        model=User
        fields=('id','username','email')


#RegistrationSerializer
class RegistrationSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the new users objects.
    '''
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        '''
        This method will create a user object upon receiving validated data
        Args:validated data(username,email,password)
        Returns: user object
        '''
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user

# LoginSerializer
class LoginSerializer(serializers.Serializer):
    '''
    A class for serilalizing and deserializing login credentials
    '''
    username=serializers.CharField()
    password=serializers.CharField()
    def validate(self,data):
        '''
        This method will validate the login credentials
        '''
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect login credentials")
        
#ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the new profiles objects.
    '''
    user = serializers.PrimaryKeyRelatedField(many=True,queryset = User.objects.all())
    class Meta:
        model=Profile
        fields=('user','avatar','bio',)

   


