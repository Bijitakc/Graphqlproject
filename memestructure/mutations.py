import graphene
from graphene_file_upload.scalars import Upload
from django.contrib.auth.decorators import login_required

from user.models import ExtendUser
from .models import Meme, Comment, Reply
from .types import MemeType, CommentType, ReplyType


class CreateMemeMutation(graphene.Mutation):
    meme = graphene.Field(MemeType)

    class Arguments:
        authorID = graphene.ID()
        title = graphene.String(required=True)
        photo = Upload(required=True)

    @classmethod
    def mutate(cls, root, info, authorID, title, photo):
        # user = info.context.user
        author = ExtendUser.objects.get(id=authorID)
        meme_ins = Meme.objects.create(title=title, author=author, photo=photo)
        return CreateMemeMutation(meme=meme_ins)


class CreateCommentMutation(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        authorID = graphene.ID()
        content = graphene.String()
        memeID = graphene.ID()

    @classmethod
    def mutate(cls, root, info, authorID, content, memeID):
        author = ExtendUser.objects.get(id=authorID)
        meme = Meme.objects.get(id=memeID)
        comment_ins = Comment.objects.create(author=author, content=content, meme=meme)
        return CreateCommentMutation(comment=comment_ins)


class CreateReplyMutation(graphene.Mutation):
    reply = graphene.Field(ReplyType)

    class Arguments:
        authorID = graphene.ID()
        content = graphene.String()
        commentID = graphene.ID()

    @classmethod
    def mutate(cls, root, info, authorID, content, commentID):
        author = ExtendUser.objects.get(id=authorID)
        comment = Comment.objects.get(id=commentID)
        reply_ins = Reply.objects.create(author=author, content=content, parent_comment=comment)
        return CreateReplyMutation(reply=reply_ins)


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


class UpdateReplyMutation(graphene.Mutation):
    reply = graphene.Field(ReplyType)

    class Arguments:
        id = graphene.ID()
        content = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, id, content):
        reply = Reply.objects.get(id=id)
        reply.content = content
        reply.save()
        return UpdateReplyMutation(reply=reply)


class DeleteMemeMutation(graphene.Mutation):
    meme = graphene.Field(MemeType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        meme = Meme.objects.get(id=id)
        meme.delete()
        return 


class DeleteCommentMutation(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        return 


class Mutation(graphene.ObjectType):
    create_meme = CreateMemeMutation.Field()
    create_comment = CreateCommentMutation.Field()
    create_reply = CreateReplyMutation.Field()
    update_meme_title = UpdateMemeMutation.Field()
    update_comment = UpdateCommentMutation.Field()
    update_reply = UpdateReplyMutation.Field()
    delete_meme = DeleteMemeMutation.Field()
    delete_comment = DeleteCommentMutation.Field()