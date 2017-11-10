# TODO

## Scheduled

### 0.2-beta.0 (Completed!)
- Class-skeleton-based annotation

### 0.3-beta.0 (Completed!)
- Const accessor
- Class handlers
- String handlers

### 0.4-beta.0
- Interface include methods (using `@include` annotation)
- `@Extends` decorator for interfaces

## Ideas
- Class Skeleton Constructor Class Handler
- Procedure acceptor wrapper
- Move everything OOP related to OOP package

## Examples

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

    @include
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

### Class Skeleton Constructor Class Handler

```python
from good.handlers.constructor import ClassSkeletonConstructor

class Person:
    construct = ClassSkeletonConstructor({'name': 'name', 'age': 'age'})

    def __init__(self, name, age):
        """
        Initializes instance
        """
        self._name = name
        self._age = age

    __repr__ = ValueStringHandler(('name', 'age'))

@Person.construct
class jim:
    name = 'Jim Slim'
    age = 23

print(jim) # prints 'Person(\'Jim Slim\', 23)'
```

### Procedure Acceptor Wrapper

```python
from good.procedure import procedure_acceptor

@procedure_acceptor
def times(n, _proc):
    _ = None
    for i in range(n):
        _ = _proc(i)
    return _

@times(100)
def _(number):
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Fizz')
    elif number % 3 == 0:
        print('Buzz')
    else:
        print(number)
```
