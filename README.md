## SE tools

### How to use?

Open python interpreter with  `python3` and then:

```python
>>> from system import System
>>> sys = System.from_file("system.se")
>>> print(sys)
System(attributes={'b', 'a', 'd', 'c'},
                objects={'x_1': (x_1: {'a': '0', 'b': '0', 'c': '0', 'd': '0', 'dec': '0'}), 'x_2': (x_2: {'a': '0', 'b': '0', 'c': '1', 'd': '1', 'dec': '0'}), 'x_3': (x_3: {'a': '1', 'b': '1', 'c': '1', 'd': '0', 'dec': '0'}), 'x_4': (x_4: {'a': '1', 'b': '1', 'c': '2', 'd': '0', 'dec': '0'}), 'x_5': (x_5: {'a': '0', 'b': '1', 'c': '0', 'd': '1', 'dec': '1'}), 'x_6': (x_6: {'a': '1', 'b': '1', 'c': '0', 'd': '2', 'dec': '1'}), 'x_7': (x_7: {'a': '0', 'b': '1', 'c': '1', 'd': '2', 'dec': '2'}), 'x_8': (x_8: {'a': '1', 'b': '0', 'c': '1', 'd': '0', 'dec': '2'})},
                core={'b', 'c'}),
                reducts={frozenset({'b', 'a', 'c'}), frozenset({'b', 'd', 'c'})},
                nondeterministic rules=[],
                consistent=True
```
