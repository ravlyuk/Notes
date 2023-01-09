from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

from snippet.schema import schema

urlpatterns = [
    # path('snippets/', include('snippet.urls'), namespace='snippets'),
    path('graphql/', GraphQLView.as_view(
        graphiql=True,
        schema=schema
    )),
    path('admin/', admin.site.urls),
]
