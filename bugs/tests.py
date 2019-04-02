from django.test import TestCase
from .models import Bugs

# Create your tests here.
class BugsTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Bugs models
    """
    
    def test_str(self):
        test_name = Bugs(name='A bug issue')
        self. assertEqual(str(test_name), 'A bug issue')