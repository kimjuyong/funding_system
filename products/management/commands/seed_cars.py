import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from products import models as product_models
from users import models as user_models


class Command(BaseCommand):

    help = "The command creates many cars"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        car_types = product_models.CarType.objects.all()
        fuel_types = product_models.FuelType.objects.all()
        seeder.add_entity(
            product_models.Car,
            number,
            {
                "name": lambda x: seeder.faker.license_plate(),
                "host": lambda x: random.choice(all_users),
                "car_type": lambda x: random.choice(car_types),
                "fuel_type": lambda x: random.choice(fuel_types),
                "guests": lambda x: random.randint(1, 6),
                "seats": lambda x: random.randint(2, 8),
                "efficiency": lambda x: random.randint(10, 100),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        facilities = product_models.Facility.objects.all()
        rules = product_models.CarRule.objects.all()
        for pk in created_clean:
            car = product_models.Car.objects.get(pk=pk)
            for i in range(3, random.randint(10, 19)):
                product_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    car=car,
                    file=f"/car_photos/{random.randint(1,22)}.jpg",
                )
            for f in facilities:
                magic_number = random.randint(1, 10)
                if magic_number % 2 == 0:
                    car.facility.add(f)
            for r in rules:
                magic_number = random.randint(1, 10)
                if magic_number % 2 == 0:
                    car.car_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} cars created!"))
