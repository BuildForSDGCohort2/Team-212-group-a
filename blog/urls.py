from django.urls import path
from .blogApi import ArticleAPI, updateArticle , CropArticlesView, StageArticlesView, ArticleFeaturedView, ArticlesListView, ArticleDetailView

urlpatterns=[
    path('api/blog/article', ArticleAPI.as_view(),name='articles'),
    path('api/blog/articles',ArticlesListView.as_view(),name="articles"),
    path('api/blog/article/featured',ArticleFeaturedView.as_view(),name="featured"),
    path('api/blog/articles/crop',CropArticlesView.as_view()),
    path('api/blog/articles/stage',StageArticlesView.as_view()),
    path('api/blog/article/update/<int:id>/',updateArticle, name="articleUpdate"),
    path('api/blog/article/detail/<slug>',ArticleDetailView.as_view()),
    

    
]