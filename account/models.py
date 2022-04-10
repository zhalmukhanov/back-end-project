from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=1)
    current_money = models.IntegerField()


class Startupper(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=1)


class UserInvestor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    current_money = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.user.username


class UserStartupper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.user.username
