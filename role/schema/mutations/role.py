import graphene
from graphene_django import DjangoObjectType

from role.models import Role

class RoleType(DjangoObjectType):
    class Meta:
        model = Role

class CreateRole(graphene.Mutation):
    id = graphene.Int()
    role_name = graphene.String()
    description =graphene.String()
    role = graphene.Field(RoleType)

    class Arguments:
        role_name = graphene.String()
        description =graphene.String()

    def mutate(self, info, role_name, description):
        role = Role(role_name=role_name, description=description)
        role.save()
        return CreateRole(role=role)

class Mutation(graphene.ObjectType):
    create_role = CreateRole.Field()





