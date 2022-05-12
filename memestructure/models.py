from django.db import models


class Meme(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(to="user.ExtendUser", on_delete=models.CASCADE, related_name="Author")
    photo = models.ImageField(upload_to='images/memephotos', null=True)

    class Meta:
        verbose_name = "Meme"
        verbose_name_plural = "Memes" 
    
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    meme = models.ForeignKey(to="Meme", on_delete=models.CASCADE)
    author = models.ForeignKey(to="user.ExtendUser", on_delete=models.CASCADE, related_name="CommentAuthor")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return self.content


class Reply(models.Model):
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(to="user.ExtendUser", on_delete=models.CASCADE, related_name="ReplyAuthor")
    parent_comment = models.ForeignKey(to="Comment", on_delete=models.CASCADE, related_name="ReplyParent")

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self) -> str:
        return self.author