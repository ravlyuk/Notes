"""
actions: create(), retrieve(), update(), partial_update(), destroy() list()
"""

from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'article-modelset', api.ArticleModelViewSet, basename='article')
urlpatterns = router.urls
