import account.models
from account.models import *
from django.db import models

from account import models as Startupper
from account.models import Startupper

class Startup(models.Model):
    startupper_id = models.ForeignKey(Startupper, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    initial_capital = models.IntegerField()
    accumulated_capital = models.IntegerField()

    def percentage(self):
        return float('{:.1f}'.format(self.accumulated_capital * 100 / self.initial_capital))

    def s_name(self):
        s = Startupper.objects.get(id = self.starupper_id_id)
        return s.first_name + " " + s.last_name