from django.urls import path
from .blogApi import CropAPI, ArticleAPI

urlpatterns=[
    path('api/blog/crop', CropAPI.as_view(),name='crops'),
    path('api/blog/article', ArticleAPI.as_view(),name='articles')
]