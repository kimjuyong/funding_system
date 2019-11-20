import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from products import models as product_models


class Command(BaseCommand):

    help = "The command creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        cars = product_models.Car.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "acurracy": lambda x: random.randint(0, 6),
                "cleanlines": lambda x: random.randint(0, 6),
                "performance": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "car": lambda x: random.choice(cars),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
