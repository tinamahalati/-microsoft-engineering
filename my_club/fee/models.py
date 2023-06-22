from django.db import models
from cycle.models import Cycle
from members.models import Member

class Fee(models.Model):
  c = models.ForeignKey(Cycle,on_delete=models.CASCADE)
  m = models.ForeignKey(Member,on_delete=models.CASCADE)
    
  price = models.CharField(max_length=12)
  discount=models.FloatField(max_length=12)
