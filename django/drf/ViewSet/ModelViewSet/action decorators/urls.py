"""
actions: create, retrieve, update, partial_update, destroy, list
"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import api

article_list = api.ArticleModelViewSet.as_view({
    'get': 'list',
    # 'put': 'create',
})

article_detail = api.ArticleModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

article_example = api.ArticleModelViewSet.as_view({
    'get': 'example',
    # 'put': 'example',
})

urlpatterns = format_suffix_patterns([
    path('article/', article_list, name="article_list"),  # action: article_list
    path('article/<int:pk>/', article_detail, name="article_detail"),  # action: article_detail
    path('article/example/<int:pk>/', article_example, name="article_example"),  # action: article_example
])
