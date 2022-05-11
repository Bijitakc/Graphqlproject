import graphene

from .query import Query
from .mutations import Mutation
from user.types import UserType


schema = graphene.Schema(query=Query, mutation=Mutation)