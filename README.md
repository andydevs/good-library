# The Good Library

A collection of programming and syntax tools for experienced Python users

_The Normal Way_
```python
from random import randint

class Person:
    """
    An ordinary person

    Author:  Steven Schmutz
    Created: 5 - 23 - 2028
    """
    def __init__(self, name,
                       age,
                       apparel='Pajamas',
                       thoughts='Crazy we\'re still using python in 2028'):
        """
        Initializes the Person object

        Params:
            - name
            - age
            - apparel (def. 'Pajamas')
            - thoughts (def. 'Crazy we\'re still using python in 2028')
        """
        self._name = name
        self._age = age
        self._apparel = apparel
        self._thoughts = thoughts

    @property
    def name(self):
        """
        Get access for _name
        """
        return self._name

    @property
    def age(self):
        """
        Get access for _age
        """
        return self._age

    def set_thoughts(self, value):
        """
        Set access for _thoughts

        :param value: value to set to
        """
        self._thoughts = value

    @property
    def apparel(self):
        """
        Get access for _apparel
        """
        return self._apparel

    @apparel.setter
    def apparel(self, value):
        """
        Set access for _apparel

        :param value: value to set
        """
        self._apparel = value

    def ask_for_thoughts(self):
        """
        Returns the person's thoughts on chance

        :return: the person's thoughts on chance
        """
        if randint(1,2) == 2: return self._thoughts
        else: return 'I\'d rather not share...'
```

_The Good Way_
```python
from good.access import Get, Set, GetSet
from good.annotation import Annotation
from good.inits import UnderscoreInit
from random import randint

# Annotations
random_outcome = Annotation('random_outcome')

class Person:
    """
    An ordinary person

    Author:  Steven Schmutz
    Created: 5 - 23 - 2028
    """
    # Properties
    name = Get('_name')
    age = Get('_age')
    thoughts = Set('_thoughts')
    apparel = GetSet('_apparel')

    # Initialize method
    __init__ = UnderscoreInit(
        required=('name', 'age'),
        defaults={
            'apparel': 'Pajamas',
            'thoughts': 'Crazy we\'re still using python in 2028'
        }
    )

    @random_outcome
    def ask_for_thoughts(self):
        """
        Returns the person's thoughts on chance

        :return: the person's thoughts on chance
        """
        if randint(1,2) == 2: return self._thoughts
        else: return 'I\'d rather not share...'
```
