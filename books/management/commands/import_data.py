from django.core.management.base import BaseCommand
from books.models import Book
from ._clean_data import clean


class Command(BaseCommand):
    help = "Import data from csv"

    def add_arguments(self, parser):
        parser.add_argument("filename", help="csv file path", type=str)

    def handle(self, *args, **options):
        data = clean(options.get("filename"))
        for row in data:
            Book.objects.create(**row)
        print(f"Utworzono {len(data)} obiektow Book")