"""
Module represents the player class of blackjack
"""
from person import Person


class Player(Person):
    """
    A class used to represent a player in the game of Blackjack, inheriting
    from the Person class.

    Attributes
    ----------
    name : str
        The name of the player, inherited from the Person class.
    amount : int
        The amount of money the player has at their disposal for placing bets.

    Methods
    -------
    __str__()
        Returns a formatted string showing the player's hand and available
        amount of money.
    place_bet()
        Prompts the player to place a bet, ensuring they have sufficient funds.
        Adjusts the player's amount if the bet is valid.
    won_bet(bet)
        Increases the player's amount by double the bet when the player wins.
    get_amount()
        Returns the current amount of money the player has.
    """

    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def __str__(self):
        print(f'Player {self.name} has {self.amount}$ at disposal.')

        if len(self.hand.get_cards()) > 1:
            print(
                f'{self.name} has {len(self.hand.get_cards())}'
                f' cards in his hand.')
        else:
            print(
                f'{self.name} has {len(self.hand.get_cards())}'
                f' card in his hand.')

        return f'{self.name}\'s hand consist of {self.hand}.'

    def place_bet(self):
        """
        Function to place the bet of the player.
        Checks whether the player has enough amount to set the bet.
        If true, the amount of the player is adjusted
        :return: int - bet
        """
        is_invalid_bet = True

        while is_invalid_bet:
            bet = input('How much you would like to bet? '
                        '\n (E.g. 20, 50, 100, ... ')
            if not bet.isdigit():
                print('Invalid input. Input is not a number. Try again! ')
                continue
            if (self.amount - int(bet)) < 0:
                print('Sry! But you have not enough money at disposal to bet'
                      ' this amount of money. Try again!')
                continue
            self.amount -= int(bet)
            return int(bet)

    def won_bet(self, bet):
        """
        Function to increment the amount of the player with winning bet.
        :param bet: the amount in the bet pot
        """
        self.amount += (bet*2)

    def get_amount(self):
        """
        Function to return the amount.
        :return: int
        """
        return self.amount
