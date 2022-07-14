from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import (
    ArticleListSerialazer,
    ArticleDetailSerialazer,
)


class ArticleViewSet(viewsets.ViewSet):
    # other actions: create, update

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleListSerialazer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleDetailSerialazer(article)
        return Response(serializer.data)
