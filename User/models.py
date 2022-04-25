from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.username


class Bider(User):
    class Meta:
        verbose_name = "bider"
        verbose_name_plural = "bider"

    def __str__(self):
        return self.username
