from django.urls import reverse

import account.models
from account.models import *
from django.db import models

from account import models as Startupper
from account.models import Startupper

class Startup(models.Model):
    startupper = models.ForeignKey(Startupper, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    initial_capital = models.IntegerField()
    accumulated_capital = models.IntegerField()

    categories = [
        ('IT', 'IT'),
        ('Ecology', 'Ecology'),
        ('Electronic', 'Electronic'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Gaming', 'Gaming'),
        ('Small Business', 'Small Business'),
        ('Other', 'Other')
    ]
    category = models.CharField(max_length=20, choices=categories, default='Other')


    def __str__(self):
        return self.title

    def percentage(self):
        return float('{:.1f}'.format(self.accumulated_capital * 100 / self.initial_capital))

    def s_name(self):
        s = Startupper.objects.get(id = self.startupper_id)
        return s.first_name + " " + s.last_name

    def get_absolute_url(self):
        return reverse('project', kwargs={'startup_id': self.pk})
