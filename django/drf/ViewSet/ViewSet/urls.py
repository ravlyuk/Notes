from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('article/', views.ArticleViewSet.as_view({'get': 'list'})),
    path('article/<int:pk>/', views.ArticleViewSet.as_view({'get': 'retrieve'})),
])
