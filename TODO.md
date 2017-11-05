# TODO

## Scheduled

### 0.2-beta.0
- Class-skeleton-based annotation

### 0.3-beta.0
- Const accessor
- Enumeration

### 0.4-beta.0
- Interface include `mixin` methods (using `@mixin` annotation)
- `@Extends` decorator for interfaces

## Ideas
- Procedure acceptance wrapper

## Examples

### Enumeration

```python
from good.enum import Enum, EnumType

@Enum('MONDAY',
      'TUESDAY',
      'WEDNESDAY',
      'THURSDAY',
      'FRIDAY',
      'SATURDAY',
      'SUNDAY')
class Weekday(EnumType):
    """
    Weekday enumeration
    """
    pass

@Enum(('RAINY', True),
      ('SNOWY', True),
      ('SUNNY', False),
      ('COLD', True))
class WeatherType(EnumType):
    """
    Weather Type enumeration
    """
    def __init__(self, name, coat):
        """
        Initializes the WeatherType

        :param name: the name of the WeatherType
        :param coat: true if WeatherType requires coat
        """
        super(EnumType, self).__init__(name)
        self.coat = coat

dayofweek = Weekday.MONDAY
weather = WeatherType.RAINY

print ('Today is', dayofweek.name.lower(), 'and it is', weather.name.lower())
if weather.coat:
    print ('You\'ll need a coat today')
```

### Class-Skeleton-Based Annotation

```python
@Annotation
class ExampleAnnotation1:
    """
    Example of an annotation class
    """
    pass

@Annotation
class ExampleAnnotation2:
    """
    Example of an annotation class with attributes

    Can define attribute which will be stored in the annotated object
    """
    __attr_string_attr = str
    __attr_number_attr = int

@ExampleAnnotation1
class ExampleImplementation1:
    """
    Implementation of annotation
    """
    pass

@ExampleAnnotation2(string_attr='Hello World', number_attr=3)
class ExampleImplementation2:
    """
    Implementation of annotation
    """
    pass
```

### Extends Decorator

```python
from good.interface import Interface, Extends, Implements

@Interface
class Walkable:
    def walk(self):
        pass

@Extends(Walkable)
@Interface
class Runnable:
    def run(self):
        pass

    @mixin
    def can_you_run(self):
        print('Yes...')

@Implements(Runnable)
class SprintRunner:
    def walk(self):
        print('Walking...')

    def run(self):
        print('Running 100m!')

usain_bolt = SprintRunner()
usain_bolt.walk() # prints 'Walking...'
usain_bolt.can_you_run() # prints 'Yes...'
usain_bolt.run() # prints 'Running 100m!'
```

### Procedure Acceptance Wrapper

```python
from good.procedure import procedure

@procedure('block_')
def each(iterable, block_):
    for value in iter(iterable):
        block_(value)

iterable = range(10)

@each(iterable)
def do(number):
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Fizz')
    elif number % 3 == 0:
        print('Buzz')
    else:
        print(number)
```
