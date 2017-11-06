"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
class BaseAnnotation:
    """
    Base class for annotations

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    _AT_prefix = '_AT_'

    # Attribute names array
    _attributes = {}

    def __init__(self, **kwargs):
        """
        Initializes Annotation with the given kwargs
        """
        # Set attributes in attr dict (created by constructor)
        for name,typ in self._attributes.items():
            if name in kwargs and type(kwargs[name]) is typ:
                self.__setattr__(name, kwargs[name])
            elif name in kwargs:
                raise Exception('Expected {typ1} for {name} attribute {attr}. Got {typ2}'.format(
                    name=type(self).__name__,
                    attr=name,
                    typ1=typ,
                    typ2=type(kwargs[name])
                ))
            else:
                raise Exception('{name} attribute {attr} not defined!'.format(
                    name=type(self).__name__,
                    attr=name))
        # TODO: Create custom error type for Attributes

    @property
    def _attr_string(self):
        """
        The attributes of the annotation
        """
        return ', '.join(
            '{name}={attr}'.format(name=attr, attr=repr(getattr(self, attr)))
            for attr in self._attributes)

    def __call__(self, obj):
        """
        Attaches the annotation to the given object

        :param obj: the object to annotate

        :return: the annotated object
        """
        setattr(obj, type(self)._AT_full_name, self)
        return obj

    def __bool__(self):
        """
        Returns true to prove existence of the Annotation
        """
        return True

    def __repr__(self):
        """
        String representation of instance
        """
        return '@{name}({attrs})'.format(
            name=type(self).__name__,
            attrs=self._attr_string)

class AnnotationType(type):
    """
    Metaclass for annotations

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    # Prefix for annotation type
    _AT_prefix = '_AT_'

    # Prefix for attribute
    _attr_prefix = '_attr_'

    @classmethod
    def from_class_skeleton(mcls, cskl):
        """
        Creates an Annotation or AnnotationType from the given cskl

        :param cskl: the class skeleton to create an annotation from

        :return: Annotation or AnnotationType from the given cskl
        """
        name = cskl.__name__
        attributes = {name[len(self._attr_prefix):]:typ # Trim prefix
                        for name,typ in cskl.__dict__.items() # Get keys
                        if name.startswith(self._attr_prefix)} # Filter by prefix

        # Create constructor
        AT_Type = AnnotationType.create(name, attributes)

        # Return constructor if attributes is not empty else annotation
        return AT_Type if len(attributes) > 0 else AT_Type()

    @classmethod
    def create(mcls, name, attrs=tuple()):
        """
        Creates a new AnnotationType and returns it

        :param name: the name of the annotation
        :param attrs: the attributes of the annotation
        """
        # Create bases and namespace dict
        bases = (BaseAnnotation,)
        nspc = dict(_attributes=attrs)

        # Return new type
        return mcls.__new__(mcls, name, bases, nspc)

    @classmethod
    def _AT_filter(mcls, value):
        """
        Filters annotation entries

        :param value: the value to filter

        :return: true if the value is an annotation
        """
        return type(type(value)) is AnnotationType

    @classmethod
    def get_all(mcls, obj):
        """
        Gets all annotations attached to the given object

        :param obj: the object to retrieve annotations from

        :return: all annotations from the given object
        """
        return tuple(filter(mcls._AT_filter, obj.__dict__.values()))

    @property
    def _AT_full_name(cls):
        """
        Return the full name of the annotation

        :return: the full name of the annotation
        """
        return cls._AT_prefix + cls.__name__

    def get(cls, obj):
        """
        Returns the annotation in the given object (or False)

        :param obj: the object to check

        :return: the annotation in the given object (or False)
        """
        return getattr(obj, cls._AT_full_name, False)

# Alias for class skeleton constructor
# (the pretty annotation decorator that you use)
Annotation = AnnotationType.from_class_skeleton
