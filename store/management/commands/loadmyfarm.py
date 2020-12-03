from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "load stores from myfarm.ch"

    def handle(self, *args, **options):
        print("this is myfarm handle")
