from django.db import models

from cycle.models import Cycle

class Member(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  national_id= models.CharField(max_length=10)
  phone_number=models.CharField(max_length=12)
  gym_id=models.CharField(max_length=14)
  c = models.ManyToManyField(Cycle)