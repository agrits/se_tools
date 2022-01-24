```python
❯ python3 example1.py
System(attributes={'c', 'b', 'a', 'd'},
                objects={'x_1': (x_1: {'a': '0', 'b': '0', 'c': '0', 'd': '0', 'dec': '0'}), 'x_2': (x_2: {'a': '0', 'b': '0', 'c': '1', 'd': '1', 'dec': '0'}), 'x_3': (x_3: {'a': '1', 'b': '1', 'c': '1', 'd': '0', 'dec': '0'}), 'x_4': (x_4: {'a': '1', 'b': '1', 'c': '2', 'd': '0', 'dec': '0'}), 'x_5': (x_5: {'a': '0', 'b': '1', 'c': '0', 'd': '1', 'dec': '1'}), 'x_6': (x_6: {'a': '1', 'b': '1', 'c': '0', 'd': '2', 'dec': '1'}), 'x_7': (x_7: {'a': '0', 'b': '1', 'c': '1', 'd': '2', 'dec': '2'}), 'x_8': (x_8: {'a': '1', 'b': '0', 'c': '1', 'd': '0', 'dec': '2'})},
                core={'c', 'b'}),
                reducts={frozenset({'c', 'b', 'd'}), frozenset({'c', 'b', 'a'})},
                nondeterministic rules=[],
                consistent=True



\begin{tabular}{|l|r|r|r|r|r|r|r|r|}
\toprule
{} &        x_1 &           x_2 &        x_3 &           x_4 &           x_5 &           x_6 &        x_7 &           x_8 \\ \hline
\midrule
x_1 &         \{\} &        \{c, d\} &  \{c, a, b\} &     \{c, a, b\} &        \{b, d\} &     \{b, a, d\} &  \{c, d, b\} &        \{c, a\} \\ \hline
x_2 &     \{c, d\} &            \{\} &  \{b, a, d\} &  \{c, d, a, b\} &        \{c, b\} &  \{c, d, a, b\} &     \{b, d\} &        \{a, d\} \\ \hline
x_3 &  \{c, a, b\} &     \{b, a, d\} &         \{\} &           \{c\} &     \{c, a, d\} &        \{c, d\} &     \{a, d\} &           \{b\} \\ \hline
x_4 &  \{c, a, b\} &  \{c, d, a, b\} &        \{c\} &            \{\} &     \{c, a, d\} &        \{c, d\} &  \{c, a, d\} &        \{c, b\} \\ \hline
x_5 &     \{b, d\} &        \{c, b\} &  \{c, a, d\} &     \{c, a, d\} &            \{\} &        \{a, d\} &     \{c, d\} &  \{c, d, a, b\} \\ \hline
x_6 &  \{b, a, d\} &  \{c, d, a, b\} &     \{c, d\} &        \{c, d\} &        \{a, d\} &            \{\} &     \{c, a\} &     \{c, d, b\} \\ \hline
x_7 &  \{c, d, b\} &        \{b, d\} &     \{a, d\} &     \{c, a, d\} &        \{c, d\} &        \{c, a\} &         \{\} &     \{b, a, d\} \\ \hline
x_8 &     \{c, a\} &        \{a, d\} &        \{b\} &        \{c, b\} &  \{c, d, a, b\} &     \{c, d, b\} &  \{b, a, d\} &            \{\} \\ \hline
\bottomrule
\end{tabular}
```
