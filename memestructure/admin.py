from django.contrib import admin
from .models import Meme, Comment, Reply


admin.site.register(Meme)
admin.site.register(Comment)
admin.site.register(Reply)
