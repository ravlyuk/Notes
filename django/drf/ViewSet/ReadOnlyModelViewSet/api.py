from rest_framework import viewsets
from .models import Article

from .serializers import (
    ArticleListSerialazer,
    ArticleDetailSerialazer,
)


class ArticleReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerialazer

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerialazer
        elif self.action == "retrieve":
            return ArticleDetailSerialazer
