from django.contrib import admin
from .models import Meme, Comment, Reply

# Register your models here.
admin.site.register(Meme)
admin.site.register(Comment)
admin.site.register(Reply)
