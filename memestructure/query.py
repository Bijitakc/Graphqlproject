import graphene
from graphene_django import DjangoListField

from .models import Meme
from .types import MemeType


class Query(graphene.ObjectType):
    all_memes = DjangoListField(MemeType)

    def resolve_all_memes(root, info):
        return Meme.objects.all()