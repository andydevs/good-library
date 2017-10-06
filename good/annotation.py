"""
The Good Library

A collection of programming and syntax tools for experienced Python users

Author:  Anshul Kharbanda
Created: 10 - 6 - 2017
"""

class Annotation:
  """
  An annotation on a class, value, or function definition

  Author:  Anshul Kharbanda
  Created: 8 - 30 - 2017
  """
  # The annotation name prefix
  _AT_prefix = '_AT_'

  @staticmethod
  def create(name):
    """
    Returns a decorator which will create an
    annotation from the given validator

    :param name: the name of the annotation

    :return: decorator which will create an
             annotation from the given validator
    """
    return lambda validator: Annotation(name, validator)

  @classmethod
  def _AT_filter(cls, key):
    """
    Filters the given key if it is an annotation type

    :param key: the key to filter

    :return: True if the key is an annotation type
    """
    return key.startswith(cls._AT_prefix)

  @classmethod
  def get_all(cls, obj):
    """
    Returns all annotation names of the object

    :param obj: the object to return the annotation of

    :return: all annotation names of the object
    """
    return tuple(filter(cls._AT_filter, obj.__dict__.keys()))

  def __init__(self, key, valid=lambda obj: True):
    """
    Creates an annotation

    :param key: the key of the annotation
    :param valid: validation function for objects to
                  annotate (default valid)
    """
    self._key = key
    self._valid = valid

  @property
  def _AT_full_name(self):
    """
    Return the full name of the annotation

    :return: the full name of the annotation
    """
    return self._AT_prefix + self._key

  def __call__(self, obj):
    """
    Applies the annotation to the given object

    :param obj: the object to apply the annotation to

    :return: the object that the annotation was applied to
    """
    if self._valid(obj):
      obj.__setattr__(self._AT_full_name, True)
      return obj
    else:
      raise Exception('Invalid object being annotated: ' + str(obj))

  def match(self, obj):
    """
    Returns true if the given object has the annotation

    :param obj: the object to check

    :return: true if the given object has the annotation
    """
    return getattr(obj, self._AT_full_name, False)
