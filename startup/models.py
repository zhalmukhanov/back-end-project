import account.models
from account.models import *
from django.db import models

from account import models as Startupper
from account.models import Startupper

class Startup(models.Model):
    starupper_id = models.ForeignKey(Startupper, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    initial_capital = models.IntegerField()
    accumulated_capital = models.IntegerField()


