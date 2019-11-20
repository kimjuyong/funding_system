from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):

    """ Car Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "manufactureCountry",
                    "pickupAddress",
                    "car_model",
                    "efficiency",
                    "car_type",
                    "fuel_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book",)}),
        ("Options", {"fields": ("guests", "seats",)}),
        ("More about Options", {"fields": ("car_rules", "facility",)}),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "manufactureCountry",
        "car_model",
        "efficiency",
        "guests",
        "seats",
        "check_in",
        "check_out",
        "instant_book",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "car_type",
        "fuel_type",
        "car_rules",
        "manufactureCountry",
    )

    filter_horizontal = (
        "facility",
        "car_rules",
    )


@admin.register(models.CarRule, models.CarType, models.Facility, models.FuelType)
class CarAdmin(admin.ModelAdmin):

    """ Car Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.cars.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
