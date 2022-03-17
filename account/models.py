from django.db import models

class Investor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date  = models.DateTimeField()
    gender = models.CharField(max_length=1)
    current_money = models.IntegerField()

class Startupper(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=1)

