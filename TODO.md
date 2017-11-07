# TODO

## Scheduled

### 0.2-beta.0 (Completed!)
- Class-skeleton-based annotation

### 0.3-beta.0
- Const accessor
- Enumeration

### 0.4-beta.0
- Interface include `mixin` methods (using `@mixin` annotation)
- `@Extends` decorator for interfaces

## Ideas
- Procedure/Routine acceptance wrapper
- Move everything OOP related to OOP package

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

@procedure('_block')
def each(iterable, _block):
    for value in iter(iterable):
        _block(value)

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
