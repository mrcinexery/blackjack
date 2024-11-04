"""
Module represents the flow of the game blackjack.
"""
from dealer import Dealer
from deck import Deck
from player import Player
from game import Game


if __name__ == "__main__":

    # Initialise the game
    deck = Deck()
    player = Player("Marc", 100)
    dealer = Dealer('Computer')
    game = Game(player, dealer, deck)

    while True:
        player.get_hand().reset_hand()
        dealer.get_hand().reset_hand()
        players_turn = True
        game_is_running = True
        game.draw_cards(player, 2)
        game.draw_cards(dealer, 2)
        print(player)
        print(dealer)

        while game_is_running:

            bet_pot = player.place_bet()

            if players_turn:
                print(f'{player.get_name()}\'s turn: ')
                while True:
                    action = player.input_action()
                    if action == 1:
                        print('Hit')
                        print('Player wants to have a new card!')
                        game.draw_cards(player, 1)
                        print(player)
                        game_is_running = (
                            game.decide_win(bet_pot, players_turn))
                        print(game_is_running)

                        if not game_is_running:
                            break

                    else:
                        print('Stay)')
                        print('Player does not want a new card!')
                        players_turn = False
                        break

            if not players_turn:
                print('Dealers turn')
                for card in dealer.get_hand().get_cards():
                    card.set_covert(False)
                print(dealer)
                while True:
                    print('Hit')
                    game.draw_cards(dealer, 1)
                    print(dealer)

                    game_is_running = game.decide_win(bet_pot, players_turn)

                    if not game_is_running:
                        break

        if not game.new_game():
            bet_pot = 0
            break
