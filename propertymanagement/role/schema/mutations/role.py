import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from role.models import Role

class RoleType(DjangoObjectType):
    class Meta:
        model = Role
class RoleInput(graphene.InputObjectType):
    id = graphene.Int()
    role_name = graphene.String()
    description =graphene.String()
class CreateRole(graphene.Mutation):
    
    # role_name = graphene.String()
    # description =graphene.String()
    # 

    class Arguments:
        input = RoleInput(required=True)
    role = graphene.Field(RoleType)

    @staticmethod
    def mutate(root, info, input):
        if Role.objects.get(role_name=input.role_name):
            raise GraphQLError('The role already exists')
            # return {'error':'The role already exists'}
        role_instance = Role(role_name=input.role_name, description=input.description)
        role_instance.save()
        return CreateRole(role=role_instance)

class Mutation(graphene.ObjectType):
    create_role = CreateRole.Field()





