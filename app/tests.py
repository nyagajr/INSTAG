from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.instagram= Profile(profile_photo = 'jj.jpg', profile_name ='insta', Bio ='funny')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.instagram,Profile))

class CommentsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.instagram= Comments(comment = 'wooooow')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.instagram,Comments))

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.tester= Image(image_name = 'NewYork', image_caption ='coolest',image = 'jj.jpg')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tester,Image))
