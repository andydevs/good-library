"""
The Good Library

The Good Library is a collection of programming and syntax tools that makes your
python code more expressive and easier to work with.

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

  def __init__(self, key):
    """
    Creates an annotation

    :param key: the key of the annotation
    """
    self._key = key

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
    obj.__setattr__(self._AT_full_name, True)
    return obj

  def match(self, obj):
    """
    Returns true if the given object has the annotation

    :param obj: the object to check

    :return: true if the given object has the annotation
    """
    return getattr(obj, self._AT_full_name, False)
