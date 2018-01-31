from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Pet(models.Model):
    kind = models.CharField(max_length=8, choices=[
        ('cat', 'Cat'),
        ('dog', 'Dog'),
    ])

    name = models.CharField(max_length=32)
    birthday = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['owner', 'name',]

    def __str__(self):
        return '{} {}'.format(self.name, self.kind)
