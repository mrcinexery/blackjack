"""
Module represents the game class of blackjack.
"""
from dealer import Dealer


class Game:
    """
    A class representing the game logic for Blackjack.

    Attributes
    ----------
    player : Player
        The player participating in the game.
    dealer : Dealer
        The dealer managing the game.
    deck : Deck
        The deck of cards used during the game.

    Methods
    -------
    new_game()
        Prompts the player to decide if they want to start a new game.
        Returns True if yes, False if no.
    print_stats()
        Prints the current card values for both the player and the dealer.
    draw_cards(person, no_of_cards)
        Draws a specified number of cards from the deck for a given person
        (player or dealer). Handles the face-down card for the dealer.
    decide_win(pot, turn)
        Decides the outcome of the game based on the total card values of the
        player and dealer. Handles the payout and win conditions.
    """

    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck

    def new_game(self):
        """
        Function to decide if players want to play a new game
        :return: True if players want to play a new game, False if they want
        not play a new game.
        """
        answer = ''
        while answer not in ['y', 'n']:
            answer = input('Would you play another game? (y/n)')
        if answer == 'y':
            if self.player.get_amount() == 0:
                print('Unfortunately the player has no money left! ')
                print('Come back tomorrow! ')
                return False
            return True
        return False

    def print_stats(self):
        """
        Function to print current value of all cards within the hand
        """
        players_total = self.player.get_hand().get_total()
        dealers_total = self.dealer.get_hand().get_total()

        print(f'{self.player.get_name()} has card value of {players_total}')
        print(f'{self.dealer.get_name()} has card value of {dealers_total}')

    def draw_cards(self, person, no_of_cards):
        """
        Function to call get_top_card (of the deck class) multiple times.
        :param person: person that is drawing
        :param no_of_cards: No of cards that are drawn
        """
        for i in range(no_of_cards):

            if isinstance(person, Dealer) and i == 1:
                person.get_hand().get_cards().append(
                    self.deck.get_top_card(True))
            else:
                person.get_hand().get_cards().append(
                    self.deck.get_top_card())

    def decide_win(self, pot, turn):
        """
        Function to check if player or dealer has won.
        :param pot: the winning bet pot
        :param turn: flag if players turn or dealers turn
        :return: True if no winning decision could be matched
        """

        blackjack = 21

        if turn:

            if self.player.get_hand().get_total() == blackjack:
                print('Player has won the game!')
                self.player.won_bet(pot)
            elif self.player.get_hand().get_total() > blackjack:
                print('Player has lost the game!')
            else:
                return True

        else:
            if self.dealer.get_hand().get_total() == 21:
                print('Dealer has won the game!')

            elif self.dealer.get_hand().get_total() > 21:
                print('Dealer has lost the game!')
                self.player.won_bet(pot)

            elif (self.dealer.get_hand().get_total()
                  > self.player.get_hand().get_total()):
                print('Dealer has won the game!')

            else:
                return True

        self.print_stats()
        return False
