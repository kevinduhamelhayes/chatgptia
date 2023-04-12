from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    puntaje = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)