from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help= "This commands inserts category data"

    def handle(self, *args, **options):
        
        # Deleting existing data
        Category.objects.all().delete()

        categories = ['Sports','Technology','Science','Art','Food']
    
        for category in categories:
            Category.objects.create(name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))
