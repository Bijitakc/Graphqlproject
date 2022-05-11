import graphene
from graphene_file_upload.scalars import Upload

from user.models import ExtendUser
from .models import Meme, Comment, Reply
from .types import MemeType, CommentType


class CreateMemeMutation(graphene.Mutation):
    meme = graphene.Field(MemeType)

    class Arguments:
        authorID = graphene.String()
        title = graphene.String(required=True)
        photo = Upload(required=True)


    @classmethod
    def mutate(cls, root, info, authorID, title, photo):
        author = ExtendUser.objects.get(id=authorID)
        meme_ins = Meme.objects.create(title=title, author=author, photo=photo)
        return CreateMemeMutation(meme_ins=meme_ins)


class UpdateMemeMutation(graphene.Mutation):
    meme = graphene.Field(MemeType)

    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
    

    @classmethod
    def mutate(cls, root, info, id, title):
        meme = Meme.objects.get(id=id)
        meme.title = title
        meme.save()
        return UpdateMemeMutation(meme=meme)


class UpdateCommentMutation(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        id = graphene.ID()
        content = graphene.String(required=True)


    @classmethod
    def mutate(cls, root, info, id, content):
        comment = Comment.objects.get(id=id)
        comment.content = content
        comment.save()
        return UpdateCommentMutation(comment=comment)


class Mutation(graphene.ObjectType):

    update_meme_title = UpdateMemeMutation.Field()
    update_comment = UpdateCommentMutation.Field()