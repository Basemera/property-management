from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# from django.conf.settings import settings.AUTH_USER_MODEL
# from django.contrib.auth.models import User

# role = models.ForeignKey('role.Role', on_delete=models.CASCADE, default=1)
# role.contribute_to_class(User, 'role')

class User(AbstractUser):
    # User = get_user_model()
    username = models.CharField(max_length=255, unique=True)
    role = models.ForeignKey('role.Role', on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False, default="0783012871")
    logged_in = models.BooleanField(default=False)
