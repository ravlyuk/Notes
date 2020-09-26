"""
actions: create(), retrieve(), update(), partial_update(), destroy() list()
"""

from rest_framework import viewsets
from .models import Article

from .serializers import (
    ArticleListSerialazer,
)


class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleListSerialazer
    queryset = Article.objects.all()
