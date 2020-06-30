import graphene
from graphene_django import DjangoObjectType

from role.models import Role
from role.schema.mutations.role import RoleType
# from role.schema.mutations import RoleType

class QueryRole(graphene.ObjectType):
    roles = graphene.List(RoleType)
    role = graphene.Field(RoleType, role_name=graphene.String())

    def resolve_roles(self, info, **kwargs):
        return Role.objects.all()

    def resolve_role(self, info, role_name):
        return Role.objects.get(role_name=role_name)