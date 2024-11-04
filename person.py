"""
Module represents the superclass person of blackjack
"""
from hand import Hand


class Person:
    """
    A superclass that represents a generic person in the game of Blackjack.
    This class is intended to be inherited by other classes such as
    Player and Dealer.

    Attributes
    ----------
    name : str
        The name of the person.
    hand : Hand
        A Hand object representing the cards held by the person.

    Methods
    -------
    __str__()
        A placeholder method for string representation, to be implemented by
        subclasses.
    get_hand()
        Returns the Hand object associated with the person.
    get_name()
        Returns the name of the person.
    input_action()
        Prompts the person to choose an action (Hit or Stay) during the game.
        Ensures valid input.
    """

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        pass

    def get_hand(self):
        """
        Function to return the hand of the person
        :return: hand obj
        """
        return self.hand

    def get_name(self):
        """
        Function to return the name of the person.
        :return: str
        """
        return self.name

    @staticmethod
    def input_action():
        """
        Function to set input action of the player.
        :return: int
        """
        action = input("What do you want to do? "
                       "\nPress 1 - Hit (Take a new card) "
                       "\nPress 2 - Stay (No more card is needed ")

        while not action.isdigit():
            print("Invalid input. Try again. ")
            action = input("What do you want to do? "
                           "\nPress 1 - Hit (Take a new card) "
                           "\nPress 2 - Stay (No more card is needed) ")
        return int(action)
