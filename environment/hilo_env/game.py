
from deck import Deck


class Game:
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.deck = Deck()
        self.deck.shuffle_draw_pile()
        self.deck.initialize()

        self.current_player = 0
        self.player_cards = []
        self.set_player_cards()

    def set_player_cards(self, cards_per_player=9):
        for player in range(self.num_players):
            self.player_cards.append([])
            for _ in range(cards_per_player):
                card = self.deck.pick_draw_pile_card()
                self.player_cards[player].append(card)
        for player in range(self.num_players):
            self.show_two_cards(player)

    def show_two_cards(self, player, card1=0, card2=4):
        self.player_cards[self.current_player][card1].set_shown()
        self.player_cards[self.current_player][card2].set_shown()

    def swap_cards(self, card, card_pos):
        self.player_cards[self.current_player][card_pos] = card
        self.check_hilo(card_pos)

    def check_hilo(self, card_pos):
        pass
        # TODO: fast algorithm for tic-tac-toe win condition
