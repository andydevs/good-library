# TODO

## Scheduled

### 0.2-beta.0 (Completed!)
- Class-skeleton-based annotation

### 0.3-beta.0 (Completed!)
- Const accessor
- Class handlers
- String handlers

### 0.4-beta.0
- Instead of using `Implements`, just decorate the class with the interface to assert if it implements the interface
    - The interface callable can also be used to check if an object implements an interface
    - The interface callable can also extend interfaces
- `default` built-in annotation for default methods
- InterfaceError

## Ideas
- Class Skeleton Constructor Class Handler
- Interface as a type of annotation

## Examples

### New Interface System

```python
from good.interface import interface

@interface
class Walkable:
    def walk(self):
        pass

@Walkable
@interface
class Runnable:
    def run(self):
        pass

    @default
    def can_you_run(self):
        print('Yes!')

@Runnable
class SprintRunner:
    def walk(self):
        print('Walking...')

    def run(self):
        print('Running 100m!')

usain_bolt = SprintRunner()
jesse_owens = SprintRunner()

usain_bolt.walk() # prints 'Walking...'
usain_bolt.can_you_run() # prints 'Yes!'
usain_bolt.run() # prints 'Running 100m!'

class Swimmer:
    def swim(self):
        print('Swimming!')

michael_phelps = Swimmer()

def have_a_race(runner1, runner2):
    Runnable(runner1)
    Runnable(runner2)
    runner1.run()
    runner2.run()

have_a_race(usain_bolt, jesse_owens)
# Prints 'Running 100m'
# Prints 'Running 100m'

have_a_race(usain_bolt, michael_phelps)
# Raises an InterfaceError '<__main__.Swimmer object at 0x123456789abcdef> (of type Swimmer) is not Runnable!'

```

### Class Skeleton Constructor Class Handler

```python
from good.handlers.init import NamedInitHandler
from good.handlers.string import ValueStringHandler
from good.handlers.constructor import ClassSkeletonConstructor

class Person:
    construct = ClassSkeletonConstructor({'name': 'name', 'age': 'age'})
    __init__ = NamedInitHandler(('name', 'age'))
    __repr__ = ValueStringHandler(('name', 'age'))

@Person.construct
class jim:
    name = 'Jim Slim'
    age = 23

# OR

class Person:
    __init__ = NamedInitHandler(('name', 'age'))
    __repr__ = ValueStringHandler(('name', 'age'))
person = ClassSkeletonConstructor({'name':'name', 'age':'age'}).bind(Person)

@person
class jim:
    name = 'Jim Slim'
    age = 23

print(jim) # prints 'Person(\'Jim Slim\', 23)'
```
