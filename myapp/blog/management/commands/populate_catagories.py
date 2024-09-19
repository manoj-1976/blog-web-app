from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This Commend inserts post data"
    
    def handle(self, *args: Any, **options: Any):
        # Delete Existing Data
        Category.objects.all().delete

        catagories = ['Sports', 'Technology', 'Science', 'Art', 'Food']
      
        for catagory_name in catagories:
            Category.objects.create(name = catagory_name)

        self.stdout.write(self.style.SUCCESS("Completed inserted data!"))


