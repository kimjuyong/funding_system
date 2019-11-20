from django.core.management.base import BaseCommand
from products.models import Facility

class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def handle(self,*args,**options):
        facilities = [
            "Leather Seats",
            "Manual Transmission",
            "Bluetooth",
            "iPod Integration",
            "Heated Seats",
            "Colored Interior",
            "Hatch",
            "Projector Headlamps",
            "Auto Dimming Mirror",
            "Cruise Control",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))