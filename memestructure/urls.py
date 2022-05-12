from django.urls import path
from memestructure.schema import schema
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView

app_name = "memestructure"

urlpatterns = [
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
    path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema)))
]
