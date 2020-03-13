from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.TextField(max_length = 40, default='Guest')
    description = models.TextField()