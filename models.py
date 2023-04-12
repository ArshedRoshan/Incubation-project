from django.db import models

# Create your models here.
class adminlogin(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)