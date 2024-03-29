# Generated by Django 3.2.13 on 2022-05-11 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memestructure', '0005_auto_20220511_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CommentAuthor', to='user.extenduser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ReplyAuthor', to='user.extenduser'),
            preserve_default=False,
        ),
    ]
