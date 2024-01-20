from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints "test crawler executed"'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Test crawler executed'))