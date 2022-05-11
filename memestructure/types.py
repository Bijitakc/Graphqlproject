from graphene_django import DjangoObjectType
from .models import Meme, Comment, Reply


class MemeType(DjangoObjectType):
    class Meta:
        model = Meme
        fields = "__all__"


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"


class ReplyType(DjangoObjectType):
    class Meta:
        model = Reply
        fields = "__all__"
