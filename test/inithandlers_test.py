"""
The Good Library

A collection of programming and syntax tools for experienced Python users

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import unittest
import good
from good.inithandlers import NamedInit, UnderscoreInit

class Person1:
    """
    Tests NamedInit

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = NamedInit(names=('name', 'age'), defaults={'age':23})

class Person2:
    """
    Tests UnderscoreInit

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = UnderscoreInit(names=('name', 'age'), defaults={'age':23})

class NamedInitTest(unittest.TestCase):
    """
    Tests named init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def test_all_names(self):
        """
        Tests all names given
        """
        self.person = Person1(name='Joe Schmoe', age=21)
        self.assertEqual(self.person.name, 'Joe Schmoe')
        self.assertEqual(self.person.age, 21)

    def test_defaults(self):
        """
        Tests only non-default names given
        """
        self.person = Person1(name='Joe Schmoe')
        self.assertEqual(self.person.name, 'Joe Schmoe')
        self.assertEqual(self.person.age, 23)

    def test_non_default_not_given(self):
        """
        Tests when non-default name is not given
        """
        with self.assertRaises(Exception):
            self.person = Person1(age=21)
            self.assertEqual(self.person.age, 21)

class UnderscoreInitTest(unittest.TestCase):
    """
    Tests underscore init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def test_all_names(self):
        """
        Tests all names given
        """
        self.person = Person2(name='Joe Schmoe', age=21)
        self.assertEqual(self.person._name, 'Joe Schmoe')
        self.assertEqual(self.person._age, 21)

    def test_defaults(self):
        """
        Tests only non-default names given
        """
        self.person = Person2(name='Joe Schmoe')
        self.assertEqual(self.person._name, 'Joe Schmoe')
        self.assertEqual(self.person._age, 23)

    def test_non_default_not_given(self):
        """
        Tests when non-default name is not given
        """
        with self.assertRaises(Exception):
            self.person = Person2(age=21)
            self.assertEqual(self.person._age, 21)
