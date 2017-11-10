"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

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
        __handle = lambda *args, **kwargs: self(instance, *args, **kwargs)
        __handle.__doc__ = self.__generate_doc__(instance, klass)

        # Return handler
        return __handle

    def __generate_doc__(self, instance, klass=None):
        """
        Returns the documentation of the handler in the bound object

        :param instance: the instance that the handler is bound to
        :param klass: the class of the instance that the handler is bound to

        :return: the documentation of the handler in the bound object
        """
        return 'Bound {handlername} in {klass} object {instance}'.format(
            handlername=type(self).__name__,
            klass=klass.__name__,
            instance=str(instance)
        )
