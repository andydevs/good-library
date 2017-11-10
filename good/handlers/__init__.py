"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
from functools import update_wrapper

class Handler:
    """
    Base class for Handler objects

    Author:  Anshul Kharbanda
    Created: 11 - 9 - 2017
    """
    def bind(self, obj):
        """
        Returns the handler bound to the given object

        :param obj: the object to bind to

        :return: handler bound to the given object
        """
        # Create bound handler
        def __bound_handler(*args, **kwargs):
            return self(obj, *args, **kwargs)
        update_wrapper(__bound_handler, self)

        # Return handler
        return __bound_handler

class InstanceHandler(Handler):
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
        # Return bound handler if instance is defined else return handler
        return self if instance is None else self.bind(instance)

class ClassHandler(Handler):
    """
    Base class for class handler classes

    Author:  Anshul Kharbanda
    Created: 11 - 9 - 2017
    """
    def __get__(self, instance, klass):
        """
        Returns the bound handler for the given class

        :param instance: an instance of the class to bind to
        :param klass: the class to bind to

        :return: bound handler
        """
        # Return bound handler if class is defined else return handler
        return self if klass is None else self.bind(klass)
