"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
import unittest
import good
from good.interface import ISpec, Interface, default
from inspect import getfullargspec
from copy import deepcopy

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------ DATA ------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class TestInterface1:
    """
    First Interface to test interface methods.
    Test single method
    """
    def method1(self, arg1):
        """
        First interface method
        """
        pass

class TestInterface2:
    """
    Second Interface to test interface methods
    Adding second method to TestInterface1
    """
    def method1(self, arg1):
        """
        First interface method
        """
        pass

    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

class TestInterface3:
    """
    Third Interface to test interface methods
    Removing first method and just having second and third
    """
    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

    def method3(self, *args):
        """
        Third interface method
        Has varargs
        """
        pass

class TestInterface4:
    """
    Fourth interface to test interface methods
    Having all three methods
    """
    def method1(self, arg1):
        """
        First interface method
        """
        pass

    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

    def method3(self, *args):
        """
        Third interface method
        """
        pass

class TestInterface5:
    """
    Fifth interface to test interface methods
    Default methods
    """
    def method1(self):
        pass

    @default
    def method4(self):
        return 'Implemented by Default'

class TestClass:
    """
    Test class to test interface methods
    """
    # Example param (should not be speccable)
    param = 2

    def __init__(self):
        """
        Initialize method (should not be speccable)
        """
        pass

    def method1(self, arg1):
        """
        First class method
        """
        pass

    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------ TESTS -----------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class ISpecTest(unittest.TestCase):
    """
    Tests the ISpec class

    Author:  Anshul Kharbanda
    Created: 10 - 19 - 2017
    """
    # Manually generated specdict for TestClass
    manual_specdict = {
        'method1': getfullargspec(TestClass.method1),
        'method2': getfullargspec(TestClass.method2)
    }

    def test_speccable(self):
        """
        Tests the speccable method
        """
        self.assertFalse(ISpec.speccable(TestClass.__init__))
        self.assertTrue(ISpec.speccable(TestClass.method1))
        self.assertFalse(ISpec.speccable(TestClass.param))

    def test_specdict(self):
        """
        Tests the specdict method
        """
        # Assert that the manual specdict equals the generated specdict
        self.assertEqual(self.manual_specdict, ISpec.specdict(TestClass))

    def test_init(self):
        """
        Tests initialization
        """
        # Assert that spec of a dict equals spec of the
        # object representing the spec
        self.assertEqual(ISpec(self.manual_specdict), ISpec(TestClass))

    def test_implemented(self):
        """
        Tests implemented method
        """
        self.assertTrue(ISpec(TestInterface1).implemented(ISpec(TestClass)))
        self.assertTrue(ISpec(TestInterface2).implemented(ISpec(TestClass)))
        self.assertFalse(ISpec(TestInterface3).implemented(ISpec(TestClass)))
        self.assertFalse(ISpec(TestInterface4).implemented(ISpec(TestClass)))

class InterfaceTest(unittest.TestCase):
    """
    Tests the Interface class

    Author:  Anshul Kharbanda
    Created: 10 - 19 - 2017
    """
    ITestInterface1 = Interface(TestInterface1)
    ITestInterface2 = Interface(TestInterface2)
    ITestInterface3 = Interface(TestInterface3)
    ITestInterface4 = Interface(TestInterface4)

    def test_initialization(self):
        """
        Tests init method
        """
        self.assertEqual(self.ITestInterface1.__name__, 'TestInterface1')
        self.assertEqual(self.ITestInterface1.__spec__, ISpec(TestInterface1))

    def test_extended(self):
        """
        Tests extended method
        """
        new_name = self.ITestInterface3.__name__
        new_spec = deepcopy(self.ITestInterface1.__spec__)
        new_spec.update(self.ITestInterface3.__spec__)
        NewInterface = self.ITestInterface1.extended(self.ITestInterface3)
        self.assertEqual(NewInterface.__name__, new_name)
        self.assertEqual(NewInterface.__spec__, new_spec)

    def test_implemented(self):
        """
        Tests implemented method
        """
        self.assertTrue(self.ITestInterface1.implemented(TestClass))
        self.assertTrue(self.ITestInterface2.implemented(TestClass))
        self.assertFalse(self.ITestInterface3.implemented(TestClass))
        self.assertFalse(self.ITestInterface4.implemented(TestClass))

    def test_call_for_assert_classes(self):
        """
        Tests class assertion __call__
        """
        self.assertEqual(self.ITestInterface1(TestClass), TestClass)

    def test_call_for_assert_instance(self):
        """
        Tests instance assertion __call__
        """
        test_inst = TestClass()
        self.assertEqual(self.ITestInterface1(test_inst), test_inst)

    def test_call_for_assert_class_error(self):
        """
        Tests erroring class assertion __call__
        """
        self.assertRaises(Exception, lambda: self.ITestInterface3(TestClass))

    def test_call_for_assert_instance_error(self):
        """
        Tests erroring instance assertion __call__
        """
        test_inst = TestClass()
        self.assertRaises(Exception, lambda: self.ITestInterface3(test_inst))

    def test_call_for_extend(self):
        """
        Tests extension __call__
        """
        CallInfc = self.ITestInterface1(self.ITestInterface3)
        ExtdInfc = self.ITestInterface1.extended(self.ITestInterface3)
        self.assertEqual(CallInfc.__spec__, ExtdInfc.__spec__)
