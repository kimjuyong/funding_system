from django.contrib import admin
from . import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):

    """ Car Admin Definition """

    pass


@admin.register(models.CarRule, models.CarType, models.Facility, models.FuelType)
class CarAdmin(admin.ModelAdmin):

    """ Car Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
