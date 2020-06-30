from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, ContentType
from role.models import Role

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        role = Role(role_name="Admin", description="Is an admin")
        role.save()
        # role_instance = Role(role_name="Property Owner", description="Is a property owner")
        # role_instance.save()

        User.objects.create_superuser(username="Admin",
            first_name="Admin",
            last_name="Admin",
            email="admin@test.com",
            password="password",
            role=role)

    def testSuperUserCreated(self):
        User = get_user_model()
        superUser = User.objects.get(username="Admin")
        self.assertEqual(superUser.is_superuser, True)
        self.assertEqual(superUser.is_active, True)

    def testOrdinaryUserCreated(self):
        User = get_user_model()
        role_instance = Role(role_name="Property Owner", description="Is a property owner")
        role_instance.save()
        user = User.objects.create_user(username="Test",
            first_name="Test",
            last_name="Test",
            email="test@test.com",
            password="password",
            role=role_instance)
        self.assertEqual(user.get_username(), "Test")

    # def testAddPermissions(self):
    #     User = get_user_model()
    #     role_instance = Role(role_name="Property Owner", description="Is a property owner")
    #     role_instance.save()
    #     content_type = ContentType.objects.get(model="user")
    #     permission = Permission(content_type=content_type, codename="property_owner", name="Property owner")
    #     permission.save()
    #     user = User.objects.create_user(username="Test",
    #         first_name="Test",
    #         last_name="Test",
    #         email="test@test.com",
    #         password="password",
    #         role=role_instance,
    #         )
    #     user.user_permissions.add(permission)
    #     has_permission = user.has_perm("auth.property_owner")
    #     self.assertEqual(has_permission, True)