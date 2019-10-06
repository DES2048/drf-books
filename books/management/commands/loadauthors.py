from django.core.management.base import BaseCommand
from filtering.models import Author


class Command(BaseCommand):
    help = "Loads authors from .txt file"

    def add_arguments(self, parser):
        parser.add_argument("filename")

    def handle(self, *args, **options):
        self._load_from_file(options['filename'])

    def _load_from_file(self, fname):
        with open(fname, 'r', encoding="utf8") as f:
            for line in f:
                Author.objects.create(name=line.rstrip())

        self.stdout.write(self.style.SUCCESS('Authors loads'))
