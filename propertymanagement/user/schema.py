from django.contrib.auth import get_user_model
import graphene
import random
import string
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from role.models import Role
from .models import User
from django.contrib.auth.models import Permission
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    username = graphene.String(required=True)
    first_name =graphene.String(required=True)
    last_name =graphene.String(required=True)
    email = graphene.String(required=True)
    phonenumber = graphene.String(required=True)
    role = graphene.Int(required=True)
    permission = graphene.String(required=False)

class CreateUser(graphene.Mutation):
    # User = get_user_model()
    user = graphene.Field(UserType)

    class Arguments:
        input = UserInput(required=True)
        # username = graphene.String(required=True)
        # first_name = graphene.String(required=True)
        # last_name = graphene.String(required=True)
        # password = graphene.String(required=True)
        # email = graphene.String(required=True)
        # role = graphene.Int(required=True)
        # permission = graphene.String(required=False)

    @staticmethod
    def mutate(root, info, input, permission=None):
        roleInstance = Role.objects.get(pk=input.role)
        if permission:
            permission = Permission.objects.get(codename=permission)
        # print(User.objects.) 
        # if User.objects.get(username=input.username):
        #     raise GraphQLError('The username already exists')
        # if User.objects.get(email=input.email):
        #     raise GraphQLError('The email already exists')
        # if User.objects.get(email=input.phonenumber):
        #     raise GraphQLError('The phone number already exists')

        user = get_user_model()(
            username=input.username,
            first_name=input.first_name,
            last_name=input.last_name,
            role=roleInstance,
            email=input.email,
            phone_number=input.phonenumber
        )
        generated_password = get_random_alphaNumeric_string(8)
        user.set_password(generated_password)
        user.save()
        mail_subject = 'Activate your account'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'username':input.username,
            'one_time_password':generated_password,
        })
        to_email = input.email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        if permission:
            user.user_permissions.add(permission)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    
def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))