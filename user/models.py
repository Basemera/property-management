from django.db import models
from django.contrib.auth.models import User

role = models.ForeignKey('role.Role', on_delete=models.CASCADE, default=1)
role.contribute_to_class(User, 'role')