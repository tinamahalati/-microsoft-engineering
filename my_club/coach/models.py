from django.db import models
from members.models import Member


class Coach(Member):
   number_of_athlete=models.IntegerField()
   number_of_class=models.IntegerField()