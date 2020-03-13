import graphene
import user.schema
import role.schema

# Mutation for sending the data to the server.
class Mutation(user.schema.Mutation, role.schema.mutation.Mutation, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(mutation=Mutation)