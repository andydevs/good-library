"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""
class AnnotationType:
    """
    Base class for annotations

    Author:  Anshul Kharbanda
    Created: 11 - 6 - 2017
    """
    _AT_prefix = '_AT_' # Prefix for annotation type
    _attr_prefix = '_attr_' # Prefix for attribute
    _attributes = {} # Attribute names array

    @classmethod
    def __AT_get_full_name(cls):
        """
        Return the full name of the annotation

        :return: the full name of the annotation
        """
        return cls._AT_prefix + cls.__name__

    @classmethod
    def get(cls, obj):
        """
        Returns the annotation in the given object (or False)

        :param obj: the object to check

        :return: the annotation in the given object (or False)
        """
        return getattr(obj, cls._AT_get_full_name(), False)

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
        setattr(obj, type(self).__AT_get_full_name(), self)
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

def get_all(obj):
    """
    Gets all annotations attached to the given object

    :param obj: the object to retrieve annotations from

    :return: all annotations from the given object
    """
    return tuple(member
            for member in obj.__dict__.values()
            if isinstance(member, AnnotationType))

def create(name, attributes=dict()):
    """
    Creates an Annotation or AnnotationType from the given info

    :param name: the name of the annotation
    :param attributes: the attributes of the annotation
    """
    AtType = type(name, (AnnotationType,), dict(_attributes=attributes))
    return AtType if len(attributes) > 0 else AtType()

def Annotation(cskl):
    """
    Decorator function for a Class Skeleton

    :param cskl: the class skeleton to create an annotation from

    :return: Annotation or AnnotationType from the given cskl
    """
    # Extract relevant info
    name = cskl.__name__
    attributes = {name[len(self._attr_prefix):]:typ # Trim prefix
                    for name,typ in cskl.__dict__.items() # Get keys
                    if name.startswith(self._attr_prefix)} # Filter by prefix

    # Create AnnotationType
    return create(name, attributes)
