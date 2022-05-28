from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'article', api.ArticleReadOnly, basename='article')
urlpatterns = router.urls
