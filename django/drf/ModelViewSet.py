# FILE: api.py

from rest_framework import viewsets
from .models import Article

from .serializers import (
    ArticleListSerialazer,
)


class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleListSerialazer
    queryset = Article.objects.all()


# FILE: serializers.py

from rest_framework import serializers
from .models import Article


class ArticleListSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "content",
            "name_author",
            "rubric",
            "published",
            "likes",
        )

# FILE: urls.py

from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'article-modelset', api.ArticleModelViewSet, basename='article')
urlpatterns = router.urls
