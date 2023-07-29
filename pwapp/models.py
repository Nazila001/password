from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


class Pass(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=100)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
