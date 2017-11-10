"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import good
import good.handlers
from good.handlers.string import ValueStringHandler, KeyValueStringHandler
import unittest

class Person1:
    """
    Test class for ValueStringHandler

    Author:  Anshul Kharbanda
    Created: 11 - 10 - 2017
    """
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    __repr__ = ValueStringHandler(('name', 'age'))

class Person2:
    """
    Test class for ValueStringHandler

    Author:  Anshul Kharbanda
    Created: 11 - 10 - 2017
    """
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    __repr__ = KeyValueStringHandler(('name', 'age'))

class ValueStringHandlerTest(unittest.TestCase):
    """
    Tests ValueStringHandler

    Author:  Anshul Kharbanda
    Created: 11 - 10 - 2017
    """
    KLS = Person1
    RPR = 'Person1(\'Joe Schmoe\', 32)'

    def setUp(self):
        """
        Sets up test case
        """
        self.person = self.KLS(name='Joe Schmoe', age=32)

    def test_repr(self):
        """
        Tests repr method
        """
        self.assertEqual(repr(self.person), self.RPR)

class KeyValueStringHandlerTest(ValueStringHandlerTest):
    """
    Tests ValueStringHandler

    Author:  Anshul Kharbanda
    Created: 11 - 10 - 2017
    """
    KLS = Person2
    RPR = 'Person2(name=\'Joe Schmoe\', age=32)'
