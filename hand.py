"""
Module represent the hand class in the game blackjack
"""


class Hand:
    """
    A class used to represent a hand of cards in the game of Blackjack.

    Attributes
    ----------
    cards : list of Card
        A list containing the card objects in the player's or dealer's hand.

    Methods
    -------
    __str__()
        Returns a string representation of the hand, showing all face-up cards,
        with face-down cards represented by 'X'.
    get_cards()
        Returns the list of cards in the hand.
    get_total()
        Calculates and returns the total value of the cards in the hand,
        handling the special case for an Ace (value 11 or 1).
    reset_hand()
        Resets the hand by clearing all cards from the hand.
    """
    def __init__(self):
        self.cards = []

    def __str__(self):
        str_cards = ''
        for idx, card in enumerate(self.cards):
            if not card.is_covert():
                str_cards += card.get_card()
            else:
                str_cards += 'X'

            if idx != len(self.cards)-1:
                str_cards += ', '

        return str_cards

    def get_cards(self):
        """
        Function to return the cards of the hand
        :return: []
        """
        return self.cards

    def get_total(self):
        """
        Function to add the value of the card within the hand
        :return: int
        """
        total = 0
        for card in self.cards:
            if total >= 11 and card.get_value() == 11:
                total += 1
            else:
                total += int(card.get_value())
        return total

    def reset_hand(self):
        """
        Function to clear the hand of each person.
        """
        self.cards = []
