from django.db import models

# Create your models here.
class recipe(models.Model):
	title = models.CharField(max_length = 100)
	prep_time = models.CharField(max_length = 50)
	cook_time = models.CharField(max_length = 50)
	ingredients = models.TextField()
