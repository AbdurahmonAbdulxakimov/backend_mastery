from django.core.management.base import BaseCommand, CommandError

from learn_menagement.models import Poll


class Command(BaseCommand):
    help = "Close the specified polls."

    def handle(self, *args, **options):

        poll = Poll.objects.update(is_published=False)

        self.stdout.write(self.style.SUCCESS("Successfully closed polls"))
