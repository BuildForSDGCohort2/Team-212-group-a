from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from .models import Article


class ArticlesListView(generics.ListAPIView):
    """

    List all articles

    Args:
        generics ([type]): [description]

    Returns:
        [type]: [description]
    """
    queryset = Article.objects.order_by("-created_at")
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


# ArticleAPI
class ArticleAPI(generics.GenericAPIView):
    '''
    This class will create a new article object once the article api endpoint is called.
    '''
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        article = serializer.validated_data


        return Response({
            "article": ArticleSerializer(article, context=self.get_serializer_context()).data,
        })

# Featured Article


class ArticleFeaturedView(generics.ListAPIView):
    queryset = Article.objects.all().filter(featured=True)
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

# Stage Articles


class StageArticlesView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        stage = data['stage']
        queryset = Article.objects.order_by(
            'created_at').filter(stage__iexact=stage)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

# Crop Articles


class CropArticlesView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        crop = data['crop']
        queryset = Article.objects.order_by(
            'created_at').filter(crop__iexact=crop)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


# Update Article
@api_view(['GET', 'PUT', 'DELETE'])
def updateArticle(request, id):
    try:
        article = Article.objects.get(pk=id)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(Article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, satus=HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.order_by('-created_at')
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)
