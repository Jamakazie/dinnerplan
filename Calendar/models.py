from django.db import models

# Create your models here.
class CalendarObject(models.Model):
	date = models.DateField()
	recipe_id = models.CharField(max_length = 100)
