import collections
from collections.abc import Sequence
from math import hypot

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
