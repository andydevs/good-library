# The Good Library

"Everyone hates software. It's messy and it gets everywhere." - Sam Gallagher 2017

The Good Library is a collection of programming and syntax tools that makes your python code more expressive and easier to work with.

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

    @property
    def thoughts(self):
        """
        Block get access for _thoughts
        """
        raise Exception('Cannot GET thoughts')
    @thoughts.setter
    def thoughts(self, value):
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
from good.interface import Interface, Implements
from good.access import Get, Set, GetSet
from good.annotation import Annotation
from good.inits import UnderscoreInit
from random import randint

@Annotation
class RandomOutcome:
    """
    Returns a random outcome

    Author:  Steven Schmutz
    Created: 10 - 19 - 2018
    """
    pass

@Interface
class Thinker:
    """
    An entity that thinks

    Author:  Steven Schmutz
    Created: 5 - 23 - 2028
    """
    def ask_for_thoughts(self):
        """
        Ask the thinker for thoughts, and it may respond

        :return: the thinker's thoughts on chance
        """
        pass

@Implements(Thinker)
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
    __init__ = UnderscoreInitHandler(
        names=('name', 'age', 'apparel', 'thoughts'),
        defaults={
            'apparel': 'Pajamas',
            'thoughts': 'Crazy we\'re still using python in 2028'
        }
    )

    @RandomOutcome
    def ask_for_thoughts(self):
        """
        Returns the person's thoughts on chance

        :return: the person's thoughts on chance
        """
        if randint(1,2) == 2: return self._thoughts
        else: return 'I\'d rather not share...'
```

## Features

### Interfaces

An Interface is a collection of methods that are to be implemented in classes that implement this Interface. The Interface class can define Interfaces from a class skeleton.

```python
from good.interface import Interface

@Interface
class MyInterface:
    def method1(self, arg1, arg2):
        pass

    def method2(self, arg2):
        pass
```

The `Implements` decorator function provides a check on the given class, ensuring that it implements the defined methods in the given interface.

```python
from good.interface import Interface, Implements

@Interface
class MyInterface:
    def method1(self, arg1, arg2):
        pass

    def method2(self, arg2):
        pass

@Implements(MyInterface)
class MyClass:
    def method1(self, arg1, arg2):
        pass

    def method2(self, arg2):
        pass
```

### Accessors

Accessors `Get`, `Set`, and `GetSet` define acceess to otherwise private properties within the class. These help indicate member variables and how they should be accessed, as in other OOP languages. All three take a single string parameter, the name of the member to access (which may be set internally)

```python
from good.access import Get, Set, GetSet

class Person:
    name = Get('_name')
    thoughts = Set('_thoughts')
    apparel = GetSet('_apparel')

    def __init__(self, name, thoughts, apparel):
        self._name = name
        self._thoughts = thoughts
        self._apparel = apparel
```

`Get` only allows get access to a member, it does not allow setting the value. `Set` only allows setting, but not getting a member. `GetSet` does both, and is mainly an indicator of access.

### Handlers

Handlers are objects that act as methods in a class. They are good for configurable, predefined functions which will otherwise be redundant to implement. Handler functionality is implemented in standard python's `__call__` method, which otherwise treats the handler like a function.

```python
from good.handlers import InstanceHandler

class MyHandler(InstanceHandler):
    def __init__(self, scale):
        self._scale = scale

    def __call__(self, instance, arg1, arg2):
        instance.result = scale*(arg1+arg2)
```

The class InstanceHandler handles binding the handler to the instance. This requires the extra `instance` parameter, which will become the bound instance of the handler

```python
from good.handlers import InstanceHandler

class MyHandler(InstanceHandler):
    def __init__(self, scale, save='last_result'):
        self._scale = scale
        self._save = save

    def __call__(self, instance, arg1, arg2):
        setattr(instance, self._save, scale*(arg1+arg2))

class MyClass:
    def __init__(self):
        self.last_result = None

    handler = MyHandler(3)
```

#### Init Handlers

A special case of redundant programming is the `__init__` method. Often times, the `__init__` is only used to set a series of member variables. Thus, they will often contain a lot of boilerplate code. The Good Library offers a few `__init__` handlers, which simplify creating `__init__` methods. `NamedInitHandler` sets member variables according to a tuple of names provided in the `names` parameter.

```python
from good.handlers.init import NameInitHandler

class Person:
    __init__ = NameInitHandler(
        names=('name', 'age', 'apparel', 'thoughts')
    )
```

Default values for these can be provided as a dict in the `defaults` parameter.

```python
from good.handlers.init import NameInitHandler

class Person:
    __init__ = NameInitHandler(
        names=('name', 'age', 'apparel', 'thoughts'),
        defaults={
            'apparel': 'Pajamas',
            'thoughts': 'Nothing at the moment...'
        }
    )
```

`UnderscoreInitHandler` is a type of `NamedInitHandler` that appends an underscore `_` to each name before setting it in the instance. `DunderInitHandler` adds a dunder, or a double-underscore `__` before each name 

### Annotations

Annotations serve as markers for functions and classes containing information that is accessible by both humans and computers.
