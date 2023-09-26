from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Comment(models.Model):
    comment = models.TextField(max_length=1000000)

class Posts(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000000)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

