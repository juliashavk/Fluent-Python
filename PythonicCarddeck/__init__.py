import collections

Card = collections.namedtuple('Card', ['rank', 'suits'])

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


#beer_card = Card('7', 'diamons')
#deck = FrenchDeck()