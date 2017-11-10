"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
from functools import update_wrapper

class InstanceHandler:
    """
    Base class for instance handler classes

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def __get__(self, instance, klass=None):
        """
        Returns the bound handler for the given instance

        :param instance: the instance to bind to
        :param klass: the class of the instance to bind to

        :return: bound handler
        """
        if instance is not None:
            def __bound_handler(*args, **kwargs):
                return self(instance, *args, **kwargs)
            update_wrapper(__bound_handler, self)
        else:
            __bound_handler = self

        # Return handler
        return __bound_handler
