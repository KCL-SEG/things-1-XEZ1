from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from things.models import Thing

class Command(BaseCommand):

    """Generate 100 random things through Faker package"""

    def __init__(self):
        super().__init__()
        self.faker = Faker("en_GB")

    def handle(self, *args, **options):
        for i in range(100):
            list = self.faker.unique.name().split()
            self.thing = Thing.objects.create(
                name = list[0],
                description = f"This is {self.faker.name()}",
                quantity = self.faker.random_int(0,100))
            self.thing.save()

        #print("WARNING: The SEED command has not been implemented yet")
