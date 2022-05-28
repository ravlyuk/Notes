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