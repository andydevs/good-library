"""
The Good Library

A collection of programming and syntax tools for experienced Python users

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
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
        def __handle(*args, **kwargs):
            """
            Bound handler

            :param *args: positional arguments
            :param **kwargs: keyword arguments
            """
            return self(instance, *args, **kwargs)

        # Return handler
        return __handle
