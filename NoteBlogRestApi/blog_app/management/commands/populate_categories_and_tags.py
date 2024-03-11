from django.core.management.base import BaseCommand
from blog_app.models import Category, Tag

class Command(BaseCommand):
    help = 'Populates the database with initial category and tag data'

    def handle(self, *args, **kwargs):
        # Adding categories
        Category.objects.get_or_create(
            category_name="Technology",
            defaults={'description': "Articles and tutorials about the latest in tech, including software, hardware, and gadgets."}
        )
        Category.objects.get_or_create(
            category_name="Travel",
            defaults={'description': "Experiences, guides, and tips for travelers exploring the globe."}
        )
        Category.objects.get_or_create(
            category_name="Food",
            defaults={'description': "Recipes, restaurant reviews, and culinary tips for food enthusiasts."}
        )
        Category.objects.get_or_create(
            category_name="Lifestyle",
            defaults={'description': "Advice, trends, and news for a well-rounded life, covering health, fashion, and culture."}
        )

        # Adding tags
        Tag.objects.get_or_create(tag_name="Python Programming")
        Tag.objects.get_or_create(tag_name="European Destinations")
        Tag.objects.get_or_create(tag_name="Healthy Recipes")
        Tag.objects.get_or_create(tag_name="Fitness Routines")
        Tag.objects.get_or_create(tag_name="Gadget Reviews")
        Tag.objects.get_or_create(tag_name="DIY Crafts")

        self.stdout.write(self.style.SUCCESS('Successfully added categories and tags'))