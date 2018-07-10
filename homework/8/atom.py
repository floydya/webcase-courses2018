
"""
>>> items = set(range(10))
>>> try:
...     with Atomic(items) as atomic:
...         atomic.append(25)
...         atomic.discard(16)
...         atomic |= {-99}
...         atomic.poop() # force failure
... except (AttributeError, IndexError, ValueError) as err:
...    pass
>>> list(sorted(items))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(items) == type(set())
True
>>> items = frozenset({1, 2, 3})
>>> with Atomic(items) as atomic:
...     a.add(42)
Traceback (most recent call last):
...
AssertionError: only mutable type of data
"""

import collections
import copy


class Atomic:

    def __init__(self, container, deep_copy=False):
        assert isinstance(container,
                          (collections.MutableSequence,
                           collections.MutableSet,
                           collections.MutableMapping)),\
            "only mutable type of data"
        self.original = container
        self.copy = copy.deepcopy if deep_copy else copy.copy

    def __enter__(self):
        self.modified = self.copy(self.original)
        return self.modified

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self.original, collections.MutableSequence):
                self.original[:] = self.modified
            elif isinstance(self.original, (collections.MutableSet, collections.MutableMapping)):
                self.original.clear()
                self.original.update(self.modified)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
