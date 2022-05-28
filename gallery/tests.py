from django.test import TestCase
from .models import *
# Create your tests here.

class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.USA = Location.objects.create(name='USA')
        self.food = categories.objects.create(name='food')
        self.culture = categories.objects.create(name='culture')

        self.food = Image.objects.create(
            name='food', location=self.USA,  description='Cheezy Burgers')

        self.food.categories.add(self.food)
        self.food.categories.add(self.culture)

    # def a testcase for instance of the food class
    def test_instance(self):
        self.food.save()
        self.assertTrue(isinstance(self.food, Image))

    def test_delete_image(self):
        self.food.save()
        self.food.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.food.save()
        self.food.name = 'burger'
        self.assertTrue(self.food.name == 'burger')

    def test_all_images(self):
        self.food.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)

    def test_search_by_category(self):
        self.food.save()
        images = Image.search_by_category('food')
        self.assertTrue(len(images) > 0)

    def test_view_location(self):
        self.food.save()
        location = Image.view_location(self.USA)
        self.assertTrue(len(location) > 0)

    def test_view_category(self):
        self.drinks.save()
        categories = Image.view_category(self.culture)
        self.assertTrue(len(categories) > 0)

class categoriesTest(TestCase):
    def setUp(self):
        self.culture = categories(category='culture')

    def test_instance(self):
        self.culture.save()
        self.assertTrue(isinstance(self.culture, categories))

class LocationTest(TestCase):
    def setUp(self):
        self.USA = Location(location='USA')

    def test_instance(self):
        self.USA.save()
        self.assertTrue(isinstance(self.USA, Location))