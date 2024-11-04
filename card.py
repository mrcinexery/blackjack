"""
Module represents the card class of Blackjack.
"""
import constants


class Card:
    """
     A class used to represent a card in the game of Blackjack.

     Attributes
     ----------
     name : str
         The name of the card (e.g., 'Ace', 'King', '7').
     suit : str
         The suit of the card (e.g., 'Hearts', 'Spades').
     value : int
         The numerical value of the card, based on the name
         (e.g., 11 for 'Ace', 10 for 'King').
     covert : bool, optional
         A flag indicating whether the card is face-down (True) or
         face-up (False). Default is False.

     Methods
     -------
     __str__()
         Returns a string representation of the card, including its
         name, suit, and value.
     get_card()
         Returns the name, suit, and value of the card as a formatted string.
     get_value()
         Returns the numerical value of the card.
     get_suit()
         Returns the suit of the card.
     set_card(suit, value)
         Updates the suit and value of the card.
     is_covert()
         Checks if the card is face-down (covert).
     set_covert(covert)
         Sets the covert status (face-down or face-up) of the card.
     """
    def __init__(self, name, suit, covert=False):
        self.name = name
        self.suit = suit
        self.value = constants.VALUES[name]
        self.covert = covert

    def __str__(self):
        return f'{self.name}|{self.suit}|{self.value}'

    def get_card(self):
        """
        Function to return card obj
        :return: name, suit and value as str
        """
        return f'{self.name}|{self.suit}|{self.value}'

    def get_value(self):
        """
        Function to return the value of a card.
        :return: value as str
        """
        return self.value

    def get_suit(self):
        """
        Function to return the suit of a card.
        :return: suit as str
        """
        return self.suit

    def set_card(self, suit, value):
        """
        Function to set name, suit and value of a card
        :param suit: suit of the card
        :param value: value of the card
        """
        self.suit = suit
        self.value = value

    def is_covert(self):
        """
        Function to check whether card is covert
        :return: True if covert
        """
        return self.covert

    def set_covert(self, covert):
        """
        Function to set the instance attribute covert.
        :param covert: boolean
        """
        self.covert = covert
