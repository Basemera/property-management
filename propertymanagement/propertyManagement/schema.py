import graphene
# from user import schema
import user.schema
# import role.schema
from role.schema.mutations.role import Mutation as RoleMutation
from role.schema.query.role import QueryRole as RoleQuery
from permissions.schema.mutations.permissions import Mutation as PermissionsMutation

# Mutation for sending the data to the server.
class Mutation(user.schema.Mutation, RoleMutation, PermissionsMutation, graphene.ObjectType):
    pass

class Query(RoleQuery, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(mutation=Mutation, query=Query)