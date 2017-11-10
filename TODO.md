# TODO

## Scheduled

### 0.2-beta.0 (Completed!)
- Class-skeleton-based annotation

### 0.3-beta.0
- Const accessor
- ToString handlers

### 0.4-beta.0
- Interface include `mixin` methods (using `@mixin` annotation)
- `@Extends` decorator for interfaces

## Ideas
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
