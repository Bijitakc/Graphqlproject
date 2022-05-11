from django.urls import path
from graphene_django.views import GraphQLView
from memestructure.schema import schema
from graphene_file_upload.django import FileUploadGraphQLView

app_name="memestructure"

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
    # path('graphql', FileUploadGraphQLView.as_view(graphiql=True))
]
