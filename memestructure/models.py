from importlib.resources import contents
from django.db import models

# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=255)
    # photo = models.FileField()

    class Meta:
        verbose_name = "Meme"
        verbose_name_plural = "Memes" 


class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    meme = models.ForeignKey(to="Meme", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    def __str__(self) -> str:
        return self.content


class Reply(models.Model):
    lol = models.TextField()
    # comment = models.ForeignKey(to="Comment", on_delete=models.CASCADE, related_name="replycontent")
    # parent_comment = models.ForeignKey(to="Comment", on_delete=models.CASCADE, related_name="Parentcomment")

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"
