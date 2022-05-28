from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

urlpatterns = format_suffix_patterns([
    path('comment/add/', api.CommentCreateViewSet.as_view({'post': 'create'})),
])





