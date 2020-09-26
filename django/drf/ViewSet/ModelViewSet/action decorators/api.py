"""
actions: create(), retrieve(), update(), partial_update(), destroy() list()
"""

from .models import Article
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import (
    ArticleListSerialazer,
    ArticleDetailSerialazer,
)


class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleListSerialazer
    queryset = Article.objects.all()

    @action(detail=True)  # , methods=['get', 'put'])
    def example(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = ArticleDetailSerialazer(article)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = [permissions.IsAdminUser]
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'example':
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
