from django.db import models

class Cycle(models.Model):
    start_cycle=models.DateField()
    end_cycle=models.DateField()
    price_cycle=models.FloatField(max_length=12)
    days_of_cycle=models.IntegerField()
