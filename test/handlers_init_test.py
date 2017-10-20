"""
The Good Library

A collection of programming and syntax tools for experienced Python users

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import unittest
import good
from good.handlers.init import NameInitHandler, UnderscoreInitHandler, DunderInitHandler

class Person1:
    """
    Tests NameInitHandler

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = NameInitHandler(names=('name', 'age'), defaults={'age':23})

class Person2:
    """
    Tests UnderscoreInitHandler

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = UnderscoreInitHandler(names=('name', 'age'), defaults={'age':23})

class Person3:
    """
    Tests DunderInitHandler

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = DunderInitHandler(names=('name', 'age'), defaults={'age':23})

class NameInitHandlerTest(unittest.TestCase):
    """
    Tests named init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    init_doc = """
        Initializes the Person1 object

        :param name: the name member of the object
        :param age: the age member of the object
        """
    def test_doc(self):
        """
        Tests documentation generator
        """
        self.assertEqual(Person1.__init__.__doc__, self.init_doc)

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

class UnderscoreInitHandlerTest(unittest.TestCase):
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

class DunderInitHandlerTest(unittest.TestCase):
    """
    Tests dunder init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def test_all_names(self):
        """
        Tests all names given
        """
        self.person = Person3(name='Joe Schmoe', age=21)
        self.assertEqual(getattr(self.person, '__name'), 'Joe Schmoe')
        self.assertEqual(getattr(self.person, '__age'), 21)

    def test_defaults(self):
        """
        Tests only non-default names given
        """
        self.person = Person3(name='Joe Schmoe')
        self.assertEqual(getattr(self.person, '__name'), 'Joe Schmoe')
        self.assertEqual(getattr(self.person, '__age'), 23)

    def test_non_default_not_given(self):
        """
        Tests when non-default name is not given
        """
        with self.assertRaises(Exception):
            self.person = Person3(age=21)
            self.assertEqual(getattr(self.person, '__age'), 21)
