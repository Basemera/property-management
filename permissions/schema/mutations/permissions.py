import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth.models import Permission, ContentType


class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission


class CreatePermission(graphene.Mutation):
    permission = graphene.Field(PermissionType)

    class Arguments:
        name = graphene.String(required=True)
        codename = graphene.String(required=True)
        content_type = graphene.String(required=True)

    def mutate(self, info, name, codename, content_type):
        content_type = ContentType.objects.get(model=content_type)
        permission = Permission.objects.create(name=name, codename=codename, content_type=content_type)
        
        permission.save()

        return CreatePermission(permission=permission)


class Mutation(graphene.ObjectType):
    permission = CreatePermission.Field()