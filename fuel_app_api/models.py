from django.db import models


class FuelStation(models.Model):
    opis_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    rack_id = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state} "