# The Good Library

A collection of programming and syntax tools for experienced Python users

```python
import good
from good.access import Get, Set, GetSet
from good.annotation import Annotation
from random import randint

# Annotations!
awesome = Annotation('awesome')
random_outcome = Annotation('random_outcome')

@awesome
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
        require=('name', 'age'),
        initialize=dict(
            apparel='Pajamas',
            thoughts='Crazy we\'re still using python in 2028'
        )
    )

    @awesome
    @random_outcome
    def ask_for_thoughts(self):
        """
        Returns the person's thoughts

        :return: the person's thoughts
        """
        if randint(1,2) == 2:
            return self.thoughts
        else:
            return 'I\'d rather not share them...'        
```
