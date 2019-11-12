from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """ Review Model Difinition """

    review = models.TextField()
    acurracy = models.IntegerField()
    cleanlines = models.IntegerField()
    performance = models.IntegerField()
    check_in = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    car = models.ForeignKey("products.Car", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review}-{self.car}"

    def rating_average(self):
        avg = (
            self.acurracy
            + self.cleanlines
            + self.performance
            + self.check_in
        ) / 4
        return round(avg, 2)

