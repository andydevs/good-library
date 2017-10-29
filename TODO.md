# TODO

## Scheduled

### 0.2-beta.0
- Const accessor
- Enumeration

### 0.3-beta.0
- Class-skeleton-based annotation
- "IExtends" decorator for interfaces

## Unscheduled
- Abstract classes
      - Figure out how to implement these

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
```

### Class-Skeleton-Based Annotation

```python
@Annotation
class ExampleAnnotation:
    """
    Example of an annotation class

    Can define properties which will be stored in the annotated object
    """
    __property1 = str
    __property2 = int

@ExampleAnnotation(property1='Hello World', property2=3)
class ExampleImplementation:
    """
    Implementation of annotation
    """
    pass
```

### IExtends Decorator

```python
from good.interface import Interface, IExtends

@Interface
class Walkable:
    def walk(self):
        pass

@IExtends(Walkable)
@Interface
class Runnable:
    def run(self):
        pass

@Implements(Runnable)
class SprintRunner:
    def walk(self):
        print('Walking...')

    def run(self):
        print('Running 100m!')

usain_bolt = SprintRunner()
usain_bolt.walk() # prints 'Walking...'
usain_bolt.run() # prints 'Running 100m!'
```
