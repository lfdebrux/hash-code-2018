#!/bin/env python3

import numpy as np

class Pizza(np.ndarray):
    r'''An object for manipulating Pizza.

    A subclass of numpy.ndarray with some descriptive methods

    >>> p = Pizza('TTTTT\nTMMMT\nTTTTT\n')
    >>> print(p)
    TTTTT
    TMMMT
    TTTTT
    >>> np.hsplit(p, [2, 3])
    [Pizza('TT;TM;TT'), Pizza('T;M;T'), Pizza('TT;MT;TT')]
    '''

    def __new__(cls, data):
        r'''
        >>> np.array_repr(Pizza('TT;TM;TT'))
        "Pizza([['T', 'T'],\n       ['T', 'M'],\n       ['T', 'T']], \n      dtype='<U1')"
        '''
        if isinstance(data, str):
            return cls.fromstr(data)
        else:
            return np.asarray(data, dtype='U1').view(cls)

    def __str__(self):
        r'''
        >>> print(Pizza([['T', 'M'], ['T', 'T']]))
        TM
        TT
        '''
        return '\n'.join(''.join(c for c in l) for l in self)

    def __repr__(self):
        r'''
        >>> repr(Pizza([['T', 'M'], ['T', 'T']]))
        "Pizza('TM;TT')"
        '''
        s = ';'.join(''.join(c for c in l) for l in self)
        return f'''Pizza({s!r})'''

    @classmethod
    def fromiter(cls, iterable, shape):
        r'''Create a Pizza from an iterator.
        >>> from io import StringIO
        >>> f = StringIO('TT\nTM\nTT\n')
        >>> np.array_repr(Pizza.fromiter(f, (3, 2)))
        "Pizza([['T', 'T'],\n       ['T', 'M'],\n       ['T', 'T']], \n      dtype='<U1')"
        '''
        p = np.empty(shape, dtype='U1')
        for i, line in zip(range(shape[0]), iterable):
            for j, c in zip(range(shape[1]), line):
                p[i][j] = c
        return cls(p)

    @classmethod
    def fromstr(cls, s):
        r'''
        >>> np.array_repr(Pizza.fromstr('TT\nTM\nTT\n'))
        "Pizza([['T', 'T'],\n       ['T', 'M'],\n       ['T', 'T']], \n      dtype='<U1')"
        >>> np.array_repr(Pizza.fromstr('TT;TM;TT'))
        "Pizza([['T', 'T'],\n       ['T', 'M'],\n       ['T', 'T']], \n      dtype='<U1')"
        '''
        s = s.translate({ord(';'): '\n'})
        return cls([list(l) for l in s.splitlines()])

    def ingredients(self):
        '''Count the ingredients in the Pizza.
        >>> Pizza([['T', 'M'], ['T', 'T']]).ingredients()
        array([1, 3])
        '''
        return np.unique(self, return_counts=True)[1]

    def tomatoes(self):
        '''Count the number of tomatoes in the Pizza.
        >>> Pizza([['T', 'M'], ['T', 'T']]).tomatoes()
        3
        '''
        return self.ingredients()[1]

    def mushrooms(self):
        '''Count the number of mushrooms in the Pizza.
        >>> Pizza([['T', 'M'], ['T', 'T']]).mushrooms()
        1
        '''
        return self.ingredients()[0]

class PizzaSlice(Pizza):

    def __new__(cls, pizza, indices):
        obj = np.asarray(pizza, dtype='U1')
        obj.indices = indices
        return obj

    def __array_finalise__(self, obj):
        if obj is None: return
        self.indices = getattr(obj, 'indices', None)

    def cut(self, indices, axis):
        pass

class Problem:
    def __init__(self, rows, columns, min_of_each, max_cells, pizza):
        self.rows = int(rows)
        self.cols = int(columns)
        self.min = int(min_of_each)
        self.max = int(max_cells)
        self.pizza = pizza

    def __repr__(self):
        return fr'''Problem({self.rows}, {self.cols}, {self.min}, {self.max}, {self.pizza!r})'''

    @classmethod
    def fromiter(cls, iterable):
        r'''Read in a single Problem from an iterable.

        >>> from io import StringIO
        >>> f = StringIO('3 5 1 6\nTTTTT\nTMMMT\nTTTTT\n')
        >>> Problem.fromiter(f)
        Problem(3, 5, 1, 6, Pizza('TTTTT;TMMMT;TTTTT'))
        '''
        p = cls.__new__(cls)
        problem_statement = next(iterable).split()
        p.rows = int(problem_statement[0])
        p.cols = int(problem_statement[1])
        p.min = int(problem_statement[2])
        p.max = int(problem_statement[3])
        p.pizza = Pizza.fromiter(iterable, (p.rows, p.cols))
        return p

class Solution:

    def __init__(self, pizza, cuts):
        self.pizza = pizza
        self.cuts = cuts
        self.hcuts = cuts[0]
        self.vcuts = cuts[1]

    def __str__(self):
        r'''
        >>> Solution(Pizza('TTTTT;TMMMT;TTTTT'), ([2, 3], []))
        3
        0 0 2 1
        0 2 2 2
        0 3 2 4
        '''

def main():
    pass

if __name__ == '__main__':
    main()
