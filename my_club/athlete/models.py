from django.db import models
from members.models import Member

class Athlete(Member):
  finger_print=models.ImageField(upload_to='images', max_length=None , blank=True , null=True)

  