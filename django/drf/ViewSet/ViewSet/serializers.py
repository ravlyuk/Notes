from rest_framework import serializers
from .models import Article


class ArticleListSerialazer(serializers.ModelSerializer):
    """ Статьи """

    class Meta:
        model = Article
        fields = (
            'title',
            'content',
            'name_author',
            'rubric',
            'published',
        )


class ArticleDetailSerialazer(serializers.ModelSerializer):
    """ 1 статья """

    class Meta:
        model = Article
        fields = '__all__'
