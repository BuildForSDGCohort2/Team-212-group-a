from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import CropSerializer, ArticleSerializer
from rest_framework.decorators import action, api_view

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

# Update Article
@api_view(['GET','PUT','DELETE'])
def updateArticle(request,id):
    try:
        article = Article.objects.get(pk=id)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=ArticleSerializer(Article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, satus = HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

