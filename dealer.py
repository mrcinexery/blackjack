"""
Module represents the dealer class of blackjack.
"""
from person import Person


class Dealer(Person):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):

        if len(self.hand.get_cards()) > 1:
            print(
                f'{self.name} has {len(self.hand.get_cards())}'
                f' cards in his hand.')
        else:
            print(
                f'{self.name} has {len(self.hand.get_cards())}'
                f' card in his hand.')

        return f'{self.name}\'s hand consist of {self.hand}.'



