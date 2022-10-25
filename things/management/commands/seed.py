from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from things.models import Thing
from things.models import User

class Command(BaseCommand):

    """Generate 100 random things and users through Faker package"""

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

    def handle(self, *args, **options):
        for i in range(100):
            list = self.faker.unique.name().split()
            self.user = User.objects.create_user(
                username = f"@{self.faker.unique.user_name()}",
                first_name = list[0],
                last_name = list[1],
                email = self.faker.unique.email(),
                password = self.faker.password(),
                bio = f"Hi! I am {list[0]} {list[1]} and I am so excited to see what this site can offer me!"
                )
            self.user.save()
        #print("WARNING: The SEED command has not been implemented yet")
