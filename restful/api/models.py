from __future__ import unicode_literals
from django.db import models


class Stack(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Users(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    stack = models.ForeignKey(Stack, on_delete=models.PROTECT, null=True)


