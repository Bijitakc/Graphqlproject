from django.urls import path
from graphene_django.views import GraphQLView
from memestructure.schema import schema

app_name="memestructure"

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
]
