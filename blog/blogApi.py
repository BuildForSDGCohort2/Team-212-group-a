from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import CropSerializer, ArticleSerializer

# CropAPI
class CropAPI(generics.GenericAPIView):
    '''
    This class will create a new crop object once the crop api endpoint is called.
    '''
    serializer_class=CropSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        crop = serializer.save()
        return Response({
            "crop":CropSerializer(Crop,context=self.get_serializer_context()).data,
           
        })


# ArticleAPI
class ArticleAPI(generics.GenericAPIView):
    '''
    This class will create a new article object once the article api endpoint is called.
    '''
    serializer_class=ArticleSerializer
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.validated_data

        return Response({
            "article":ArticleSerializer(article,context=self.get_serializer_context()).data,  
        })

