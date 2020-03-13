from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.TextField(max_length = 40)
    description = models.TextField()