import graphene
from graphene_django import DjangoListField, DjangoObjectType
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


class Query(graphene.ObjectType):

    all_memes = DjangoListField(MemeType)

    def resolve_all_memes(root, info):
        return Meme.objects.all()

    all_comments = DjangoListField(CommentType)

    def resolve_all_comments(root, info):
        return Comment.objects.all()

    all_replies = DjangoListField(ReplyType)

    def resolve_all_replies(root, info):
        return Reply.objects.all()


# To update
class CommentMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        content = graphene.String(required=True)

    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, root, info, id, content):
        comment = Comment.objects.get(id=id)
        comment.content = content
        comment.save()
        return CommentMutation(comment=comment)


class Mutation(graphene.ObjectType):

    update_comment = CommentMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)