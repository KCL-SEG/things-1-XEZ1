from things.models import Thing
from django.core.management.base import BaseCommand, CommandError
"""Remove all users except super users and staff accounts"""




class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        for thing in Thing.objects.all():
            thing.delete()
