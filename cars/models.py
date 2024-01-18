from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.brand
