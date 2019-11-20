from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CarType(AbstractItem):

    """ CarType Model Definition """

    class Meta:
        verbose_name = "Car Type"


class CarRule(AbstractItem):

    """ CarRule Model Definition """

    class Meta:
        verbose_name = "Car Rule"


class FuelType(AbstractItem):

    """ FuelType Model Definition """

    class Meta:
        verbose_name = "Fuel Type"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="car_photos")
    car = models.ForeignKey("Car", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Car(core_models.TimeStampedModel):

    """ Car Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    manufactureCountry = CountryField()
    pickupAddress = models.CharField(max_length=200)
    guests = models.IntegerField()
    car_model = models.CharField(max_length=140)
    seats = models.IntegerField()
    efficiency = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    instant_book = models.BooleanField(default=True)
    host = models.ForeignKey(
        "users.User", related_name="cars", on_delete=models.CASCADE
    )
    car_type = models.ForeignKey(
        "CarType", on_delete=models.SET_NULL, related_name="cars", null=True, blank=True
    )
    fuel_type = models.ForeignKey(
        "FuelType",
        on_delete=models.SET_NULL,
        related_name="cars",
        null=True,
        blank=True,
    )
    car_rules = models.ManyToManyField("CarRule", related_name="cars", blank=True)
    facility = models.ManyToManyField("Facility", related_name="cars", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.rating_average()
            return all_rating / len(all_reviews)
        return 0
