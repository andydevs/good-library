"""
The Good Library

A collection of programming and syntax tools for experienced Python users

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import good
from good.access import GetSet, Get, Set
import unittest

class Person:
    """
    Example class to test use of GetSet, Get, and Set descriptors

    Author:  Anshul Kharbanda
    Created: 10 - 6 - 2017
    """
    name = Get('_name')
    age = Get('_age')
    thoughts = Set('_thoughts')
    apparel = GetSet('_apparel')

    def __init__(self, name, age):
        """
        Initializes the person with the given name and age

        :param name: the name of the person
        :param age: the age of the person
        """
        self._name = name
        self._age = age
        self._thoughts = 'Not thinking anything...'
        self._apparel = 'Totally Naked!'

class GetSetBaseTest(unittest.TestCase):
    """
    Base class for GetSet, Get, and Set unit tests

    Author:  Anshul Kharbanda
    Created: 10 - 6 - 2017
    """
    def setUp(self):
        """
        Sets up the test
        """
        self.person = Person('Joe Schmoe', 24)

class GetSetTest(GetSetBaseTest):
    """
    Tests the GetSet object

    Author:  Anshul Kharbanda
    Created: 10 - 6 - 2017
    """
    def test_get(self):
        """
        Tests the __get__ method
        """
        self.assertEqual(self.person.apparel, 'Totally Naked!')

    def test_set(self):
        """
        Tests the __set__ method
        """
        self.person.apparel = 'Mr. Meeseeks shirt'
        self.assertEqual(self.person._apparel, 'Mr. Meeseeks shirt')
        self.assertEqual(self.person.apparel, 'Mr. Meeseeks shirt')

class GetTest(GetSetBaseTest):
    """
    Tests the Get object

    Author:  Anshul Kharbanda
    Created: 10 - 6 - 2017
    """
    def test_get(self):
        """
        Tests the __get__ method
        """
        with self.assertRaises(Exception, msg='Get access _name cannot be set'):
            self.person.name = 'Bob Dole'

class SetTest(GetSetBaseTest):
    """
    Tests the Set object

    Author:  Anshul Kharbanda
    Created: 10 - 6 - 2017
    """
    def test_set(self):
        """
        Tests the __set__ method
        """
        with self.assertRaises(Exception, msg='Set access _name cannot be get'):
            print(self.person.thoughts)
