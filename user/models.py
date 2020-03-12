from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField(max_length = 40)
    last_name = models.TextField(max_length = 40)
    email = models.EmailField()
    role = models.ForeignKey('role.Role', on_delete=models.CASCADE)