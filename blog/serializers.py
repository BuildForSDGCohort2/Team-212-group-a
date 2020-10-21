from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Crop, Article, Stage
from accounts.serializers import UserSerializer


# CropSerializer
class CropSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the Crop objects.
    '''
    class Meta:
        model = Crop
        fields = ('name',)

# Stage Serializer


class StageSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all new Stage objects.
    '''
    class Meta:
        model = Stage,
        fields = ['name',]


# ArticleSerializer
class ArticleSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the new articles objects.
    '''
#     crop = CropSerializer(read_only=True,
#    )
#     stage = StageSerializer(read_only=True,
#          )
#     farmer = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ( 'crop', 'farmer','title', 'stage', 'content', 'cropimage')
