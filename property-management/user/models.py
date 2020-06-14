from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# from django.conf.settings import settings.AUTH_USER_MODEL
# from django.contrib.auth.models import User

# role = models.ForeignKey('role.Role', on_delete=models.CASCADE, default=1)
# role.contribute_to_class(User, 'role')

class User(AbstractUser):
    # User = get_user_model()
    role = models.ForeignKey('role.Role', on_delete=models.CASCADE, default=1)
