from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):
    
    """ List Model Definition """

    name = models.CharField(max_length=80)
    cars = models.ManyToManyField("products.Car", blank=True)
    user = models.ForeignKey("users.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def count_cars(self):
        return self.cars.count()
    
    count_cars.short_description = "Number Of Cars"