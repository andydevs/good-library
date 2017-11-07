"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import good
from good.annotation import AnnotationSet, AnnotationType, create, Annotation, get_all
import unittest

class ExampleAnnotation1(AnnotationType):
    """
    Tests extending AnnotationType

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    _attributes = dict(name=str, number=int)

# Test create function
ExampleAnnotation2 = create('ExampleAnnotation2', dict(name=str, number=int))
EmptyExampleAnnotation2 = create('EmptyExampleAnnotation2')

@Annotation
class ExampleAnnotation3:
    """
    Tests Annotation Decorator

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    _attr_name = str
    _attr_number = int

@Annotation
class EmptyExampleAnnotation3:
    """
    Tests Annotation Decorator

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    pass

class AnnotationTypeTest(unittest.TestCase):
    """
    Tests AnnotationType

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    ATT = ExampleAnnotation1

    def setUp(self):
        """
        Sets up test case
        """
        self.At = self.ATT(name='Joe Schmoe', number=2)
        self.example = self.At(lambda val: val + 2)

    def test_properties(self):
        """
        Tests properties method
        """
        self.assertEqual(self.ATT._AT_prefix, '_AT_')
        self.assertEqual(self.ATT._attributes, dict(name=str, number=int))

    def test_get_full_name(self):
        """
        Tests get_full_name method
        """
        self.assertEqual(self.ATT._AT_get_full_name(), '_AT_'+self.ATT.__name__)

    def test_init(self):
        """
        Tests init method
        """
        self.assertIs(type(self.At), self.ATT)
        self.assertEqual(self.At.name, 'Joe Schmoe')
        self.assertTrue(self.At.number, 2)
        with self.assertRaises(Exception):
            self.ATT(name='Joe Schmoe')
        with self.assertRaises(Exception):
            self.ATT(number=2)
        with self.assertRaises(Exception):
            self.ATT(salad=True)

    def test_bool(self):
        """
        Tests bool method
        """
        self.assertTrue(self.At)

    def test_repr(self):
        """
        Tests repr method
        """
        self.assertEqual(repr(self.At),
            '@'+self.ATT.__name__+'(name=\'Joe Schmoe\', number=2)')

    def test_call(self):
        """
        Tests call method
        """
        self.assertEqual(getattr(self.example, '_AT_'+self.ATT.__name__), self.At)

    def test_get(self):
        """
        Tests get method
        """
        self.assertEqual(self.ATT.get(self.example), self.At)

class CreateConstructorTest(AnnotationTypeTest):
    """
    Tests create constructor method

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    ATT = ExampleAnnotation2
    ATE = EmptyExampleAnnotation2

    def setUp(self):
        """
        Sets up test case
        """
        super(CreateConstructorTest, self).setUp()
        self.example2 = self.ATE(lambda val: val*2)

    def test_empty(self):
        """
        Tests empty method
        """
        self.assertTrue(isinstance(self.ATE, AnnotationType))

    def test_empty_call(self):
        """
        Tests empty_call method
        """
        self.assertEqual(getattr(self.example2, '_AT_'+type(self.ATE).__name__), self.ATE)

    def test_empty_get(self):
        """
        Tests get method
        """
        self.assertEqual(self.ATE.get(self.example2), self.ATE)

class AnnotationConstructorTest(CreateConstructorTest):
    """
    Tests Annotation constructor method

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    ATT = ExampleAnnotation3
    ATE = EmptyExampleAnnotation3

class GetAllTest(unittest.TestCase):
    """
    Tests get_all method
    """
    def test_get_all(self):
        """
        Tests get_all method
        """
        method = lambda val: val*2
        at1 = ExampleAnnotation1(name='Joe Schmoe', number=2)
        at2 = ExampleAnnotation2(name='Jane Shane', number=4)
        at3 = ExampleAnnotation3(name='John Scohn', number=4)
        at4 = EmptyExampleAnnotation2
        method = at4(at3(at2(at1(method))))
        atset = AnnotationSet(method, {at1, at2, at3, at4})
        self.assertEqual(get_all(method), atset)
