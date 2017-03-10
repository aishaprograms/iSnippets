from django.db import models

# Create your models here.
class User(models.Model):
    first_name = Models.CharField(max_length=256, blank=False, null=False)