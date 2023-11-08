from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=50)
    drink_category = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' - ' + self.drink_category