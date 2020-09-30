from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Crop, Article


# CropSerializer
class CropSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the Crop objects.
    '''
    class Meta:
        model=Crop
        fields=('name',)


#ArticleSerializer
class ArticleSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the new articles objects.
    '''
    crop = serializers.PrimaryKeyRelatedField(many=True,queryset = Crop.objects.all())
    class Meta:
        model=Article
        fields=('title','crop','farmer','content','cropimage')

   