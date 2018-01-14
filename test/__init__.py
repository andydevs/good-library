"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
from .handlers_test import (
    NameInitHandlerTest,
    UnderscoreInitHandlerTest,
    DunderInitHandlerTest,
    ValueStringHandlerTest,
    KeyValueStringHandlerTest )
from .access_test import (
    GetTest,
    SetTest,
    GetSetTest,
    ConstTest )
from .annotation_test import (
    AnnotationTypeTest,
    CreateConstructorTest,
    AnnotationConstructorTest,
    GetAllTest )
from .interface_test import (
    ISpecTest,
    InterfaceTest )
from unittest import main as unittest_main
