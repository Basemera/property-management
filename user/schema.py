from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from role.models import Role


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        role = graphene.Int(required=True)

    def mutate(self, info, username, first_name, last_name, password, email, role):
        roleInstance = Role.objects.get(pk=role)
        user = get_user_model()(
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=roleInstance,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()