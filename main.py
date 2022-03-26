# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Sequence

from PythonicCarddeck import Card, FrenchDeck, Vector
#from random import choice

beer_card = Card('7', 'diamonds')
deck = FrenchDeck()
#print(beer_card)
#print(choice(deck))

#for card in reversed(deck): #doctest: +ELLIPSIS
#    print(card)

#print(Card('Q', 'hearts') in deck)

suit_values = dict(spades = 3, hearts= 2, diamonds= 1, clubs = 0)


def spades_high(crd):
    rank_value =FrenchDeck.ranks.index(crd.rank)
    return rank_value * len(suit_values) + suit_values[crd.suit] #TODO

for card in sorted(deck, key = spades_high): #doctest: +ELLIPSIS
    print(card)


vec1 = Vector(2,3)
print(issubclass(FrenchDeck,Sequence))
print(isinstance(FrenchDeck(),Sequence))


print(vec1)


