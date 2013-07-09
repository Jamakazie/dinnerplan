from django.db import models

# Create your models here.
class List(models.Model):
	items = models.TextField()
