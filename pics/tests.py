from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):

    # set up method
    def setUp(self):
        self.nairobi= Image(image_name = 'Nairobi', description = 'city under the sun', location = 'Nairobi', category = 'cities')


# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Image))


# testing save method
    def test_save_method(self):
        self.nairobi.save_image()
        images = image.objects.all()
        self.assertTrue(len(images) > 0)