# Generated by Django 3.2.13 on 2022-05-11 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memestructure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='lol',
        ),
        migrations.AddField(
            model_name='reply',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='parent_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Parentcomment', to='memestructure.comment'),
            preserve_default=False,
        ),
    ]
