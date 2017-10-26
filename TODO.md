# TODO

## Scheduled

### 0.2-beta.0
    - Create Const accessor
    - Create Enumeration (see [Example 1](#example-1))

### 0.3-beta.0
    - Create class-skeleton-based annotation (see [Example 2](#example-2))

## Examples

### Example 1

_enumeration type_

```python
@Enum('MONDAY',
      'TUESDAY',
      'WEDNESDAY',
      'THURSDAY',
      'FRIDAY',
      'SATURDAY',
      'SUNDAY')
class Weekday:
    pass

dayofweek = Weekday.MONDAY
```

### Example 2

_class-skeleton-based annotation_

```python
@Annotation
class ExampleAnnotation:
    """
    Example of an annotation class

    Can define properties which will be stored in the annotated object
    """
    __meta_property1 = str
    __meta_property2 = int

@ExampleAnnotation(property1='Hello World', property2=3)
class ExampleImplementation:
    pass
```
