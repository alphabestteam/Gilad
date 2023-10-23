from django.test import TestCase, Client
from .models import Person, Parent
import unittest
# Create your tests here.

class TestPersonMethods(unittest.TestCase):

    def setUp(self):
        Person.objects.create(name = "sderottt", id = 106, birth_date = '1990-05-15', city = "ashkelon")
        Person.objects.create(name = "nahariaaa", id = 107, birth_date = '2012-05-15', city = "ashkelon")

    def test_is_over_18(self):
        """
        test that check if person is over 18 years
        """
        # Get a Person instance with a date of birth for someone under 18
        over_18 = Person.objects.get(name="sderottt")

        # Get a Person instance with a date of birth for someone over 18
        under_18 = Person.objects.get(name="nahariaaa")

        self.assertFalse(under_18.is_over_18())
        self.assertTrue(over_18.is_over_18())

        over_18.delete()
        under_18.delete()


class ParentFunctionalityTest(TestCase):
    def get_all_parents_test(self):
        parent = Parent.objects.create(name = "sderottt", id = 106, birth_date = '1990-05-15', city = "ashkelon")
        c = Client()

        # Make a GET request to the 'getAllPeople' view (update this URL according to your project's URL configuration)
        response = c.get('people/getAllParents')

        # Assert the response status code, e.g., 200 for a successful request
        data = response.content.decode('utf-8')
        print(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, "")
