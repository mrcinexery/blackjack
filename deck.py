"""
Module represents the deck class of blackjack.
"""
import random
from card import Card
import constants


class Deck:
    """
      A class used to represent a deck of cards for the game of Blackjack.

      Attributes
      ----------
      cards : list of Card
          A list that holds all the card objects in the deck, initially
          populated with standard Blackjack cards.

      Methods
      -------
      __str__()
          Returns a string representation of the entire deck, with each card
          listed on a new line.
      get_top_card(covert=False)
          Removes and returns the top card from the deck. If `covert` is True,
          the card will be face-down.
      shuffle()
          Shuffles the deck of cards randomly.
      get_cards()
          Returns the current list of cards in the deck.
      get_size()
          Returns the number of cards remaining in the deck.
      set_cards(cards)
          Replaces the current cards in the deck with a new list of cards.
    """
    def __init__(self):
        self.cards = []
        for suit in constants.SUITS:
            for name in constants.RANKS:
                self.cards.append(Card(name, suit))
        self.shuffle()

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])

    def get_top_card(self, covert=False):
        """
        Function to return the top card of the deck
        :return: card
        """
        if len(self.cards) > 0:
            card = self.cards.pop()
            if covert:
                card.set_covert(covert)
            return card
        return None

    def shuffle(self):
        """
        Function to shuffle the cards of a deck randomly.
        :return: list - shuffled deck
        """
        random.shuffle(self.cards)

    def get_cards(self):
        """
        Function to return cards of the card deck.
        :return: cards
        """
        return self.cards

    def get_size(self):
        """
        Function to return the size of the card deck.
        :return: size of deck
        """
        return len(self.cards)

    def set_cards(self, cards):
        """
        Function to set cards within a deck
        :param cards: cards
        """
        self.cards = cards
