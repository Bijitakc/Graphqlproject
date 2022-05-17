from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from memestructure.models import Meme

post_save.connect(post_save_subscription, sender=Meme, dispatch_uid="meme_post_save")
post_delete.connect(post_delete_subscription, sender=Meme, dispatch_uid="meme_post_delete")
