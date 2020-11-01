from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import  Article
from accounts.serializers import UserSerializer

# ArticleSerializer
class ArticleSerializer(serializers.ModelSerializer):
    '''
    A class that will be used to serialize and deserialize all the new articles objects.
    '''
    class Meta:
        model = Article
        fields = '__all__'
        lookup_field="slug"

