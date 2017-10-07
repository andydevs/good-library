"""
The Good Library

A collection of programming and syntax tools for experienced Python users

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import good
from good.annotation import Annotation
import unittest

class AnnotationTest(unittest.TestCase):
    """
    Tests the Annotation object

    Author:  Anshul Kharbanda
    Created: 10 - 6 - 2017
    """
    def setUp(self):
        """
        Sets up each test
        """
        self.annotation = Annotation('annotation')
        self.annotation2 = Annotation('annotation2')

    def test_AT_full_name(self):
        """
        Tests the _AT_full_name method
        """
        self.assertEqual(self.annotation._AT_full_name, '_AT_annotation')

    def test_call(self):
        """
        Tests the __call__ method
        """
        self.example = self.annotation(lambda val: val + 2)
        self.assertIn('_AT_annotation', self.example.__dict__)

    def test_match(self):
        """
        Tests the match function
        """
        self.example1 = self.annotation(lambda val: val + 2)
        self.example2 = lambda val: val + 3
        self.assertTrue(self.annotation.match(self.example1))
        self.assertFalse(self.annotation.match(self.example2))

    def test_AT_filter(self):
        """
        Tests the _AT_filter method
        """
        self.assertTrue(Annotation._AT_filter('_AT_annotation'))
        self.assertTrue(Annotation._AT_filter('_AT_also_annotation'))
        self.assertFalse(Annotation._AT_filter('not_an_annotation'))
        self.assertFalse(Annotation._AT_filter('__init__'))

    def test_get_all(self):
        """
        Tests the get_all method
        """
        self.example0 = lambda val: val+2
        self.example1 = self.annotation(lambda val: val+2)
        self.example2 = self.annotation2(self.annotation(lambda val: val+2))
        self.assertCountEqual(Annotation.get_all(self.example0), [])
        self.assertCountEqual(Annotation.get_all(self.example1), ['_AT_annotation'])
        self.assertCountEqual(Annotation.get_all(self.example2), ['_AT_annotation', '_AT_annotation2'])
