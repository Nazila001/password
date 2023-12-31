from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, default=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
