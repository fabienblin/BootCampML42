import numpy as np


class NumPyCreator():
    def from_list(self, lst):
        s = np.array(lst)
        print(s)
        return s

    def from_tuple(self, tpl):
        s = np.array(tpl)
        print(s)
        return s

    def from_iterable(self, itr):
        s = np.array(itr)
        print(s)
        return s

    def from_shape(self, shape):
        s = np.zeros(shape)
        print(s)
        return s

    def random(self, shape):
        s = np.random.random(shape)
        print(s)
        return s

    def identity(self, n):
        s = np.identity(n)
        print(s)
        return s

"""
npc = NumPyCreator()
shape = (3,5)

from_list = npc.from_list([[1,2,3],[6,3,4]])
from_tuple = npc.from_tuple(("a", "b", "c"))
from_iterable = npc.from_iterable(range(5))
from_shape = npc.from_shape(shape)
random = npc.random(shape)
identity = npc.identity(4)
"""
