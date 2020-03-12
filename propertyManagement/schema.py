import graphene
import user.schema

# Mutation for sending the data to the server.
class Mutation(user.schema.Mutation, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(mutation=Mutation)