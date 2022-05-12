from graphene_django import DjangoObjectType
from .models import ExtendUser


class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = ["username", "email"]