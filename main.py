# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PythonicCarddeck import Card, FrenchDeck
from random import choice

beer_card = Card('7', 'diamons')
deck = FrenchDeck()
#print(beer_card)
#print(choice(deck))

for card in reversed(deck): #doctest: +ELLIPSIS
    print(card)

print(Card('Q', 'hearts') in deck)
