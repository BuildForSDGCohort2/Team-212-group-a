from django.urls import path
from .blogApi import CropAPI, ArticleAPI, updateArticle ,CategoryArticles, StageApi

urlpatterns=[
    path('api/blog/crop', CropAPI.as_view(),name='crops'),
    path('api/blog/stage', StageApi.as_view(),name='stage'),
    path('api/blog/article', ArticleAPI.as_view(),name='articles'),
    path('api/blog/article/update/<int:id>/',updateArticle, name="articleUpdate"),
    path('api/blog/articles/<str:stage>/',CategoryArticles.as_view({
    'get': 'list',
}),name='bycategories'),
    
]