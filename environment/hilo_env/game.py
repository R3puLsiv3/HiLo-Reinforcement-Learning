
from deck import Deck, Card, DUMMY_COLOR

TOP_LEFT = 0
TOP_MID = 1
TOP_RIGHT = 2
MID_LEFT = 3
CENTER = 4
MID_RIGHT = 5
LOW_LEFT = 6
LOW_MID = 7
LOW_RIGHT = 8


class Game:
    def __init__(self, num_players=2):
        self.num_players = num_players

        # Setting up the card deck.
        self.deck = Deck()
        self.deck.shuffle_draw_pile()
        self.deck.initialize()

        # Setting up the cards in front of each player.
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

    def show_two_cards(self, card1_pos: int = 0, card2_pos: int = 4) -> None:
        """
        Flips the hidden cards at position card_pos1 and card_pos2 at the beginning of the game. By default, the middle
        and top left card are chosen, since this is assumed to be one of the optimal starting moves.

        :param card1_pos: Position of the first card to be flipped over.
        :param card2_pos: Position of the second card to be flipped over.
        """
        card1 = self.player_cards[self.current_player][card1_pos]
        card1.show()
        self.check_hilo(card1_pos, card1.color)
        card2 = self.player_cards[self.current_player][card2_pos]
        card2.show()
        self.check_hilo(card2_pos, card2.color)

    def swap_cards(self, card: Card, card_pos: int) -> None:
        """
        Swaps the card at position card_pos with the given card and checks if the swap resulted in a HiLo.

        :param card: New card replacing the previous.
        :param card_pos: Position of the card to be swapped.
        """
        self.player_cards[self.current_player][card_pos] = card
        self.check_hilo(card_pos, card.color)

    def check_hilo(self, card_pos, card_color):
        cards = self.player_cards[self.current_player]
        match card_pos:
            case 0:
                if cards[TOP_MID].color == card_color and cards[TOP_RIGHT].color == card_color:
                    self.drop_line(TOP_LEFT, TOP_MID, TOP_RIGHT)
                elif cards[MID_LEFT].color == card_color and cards[LOW_LEFT].color == card_color:
                    self.drop_line(TOP_LEFT, MID_LEFT, LOW_LEFT)
                elif cards[CENTER].color == card_color and cards[LOW_RIGHT].color == card_color:
                    self.drop_line(TOP_LEFT, CENTER, LOW_RIGHT, diagonal=True)
            case 1:
                if cards[TOP_LEFT].color == card_color and cards[TOP_RIGHT].color == card_color:
                    self.drop_line(TOP_LEFT, TOP_MID, TOP_RIGHT)
                elif cards[CENTER].color == card_color and cards[LOW_MID].color == card_color:
                    self.drop_line(TOP_MID, CENTER, LOW_MID)
            case 2:
                if cards[TOP_LEFT].color == card_color and cards[TOP_MID].color == card_color:
                    self.drop_line(TOP_LEFT, TOP_MID, TOP_RIGHT)
                elif cards[MID_RIGHT].color == card_color and cards[LOW_RIGHT].color == card_color:
                    self.drop_line(TOP_RIGHT, MID_RIGHT, LOW_RIGHT)
                elif cards[LOW_LEFT].color == card_color and cards[TOP_RIGHT].color == card_color:
                    self.drop_line(LOW_LEFT, CENTER, TOP_RIGHT, diagonal=True)
            case 3:
                if cards[CENTER].color == card_color and cards[MID_RIGHT].color == card_color:
                    self.drop_line(MID_LEFT, CENTER, MID_RIGHT)
                elif cards[TOP_LEFT].color == card_color and cards[LOW_LEFT].color == card_color:
                    self.drop_line(TOP_LEFT, MID_LEFT, LOW_LEFT)
            case 4:
                if cards[MID_LEFT].color == card_color and cards[MID_RIGHT].color == card_color:
                    self.drop_line(MID_LEFT, CENTER, MID_RIGHT)
                elif cards[TOP_MID].color == card_color and cards[LOW_MID].color == card_color:
                    self.drop_line(TOP_MID, CENTER, LOW_MID)
                elif cards[TOP_LEFT].color == card_color and cards[LOW_RIGHT].color == card_color:
                    self.drop_line(TOP_LEFT, CENTER, LOW_RIGHT, diagonal=True)
                elif cards[LOW_LEFT].color == card_color and cards[TOP_RIGHT].color == card_color:
                    self.drop_line(LOW_LEFT, CENTER, TOP_RIGHT, diagonal=True)
            case 5:
                if cards[MID_LEFT].color == card_color and cards[CENTER].color == card_color:
                    self.drop_line(MID_LEFT, CENTER, MID_RIGHT)
                elif cards[TOP_RIGHT].color == card_color and cards[LOW_RIGHT].color == card_color:
                    self.drop_line(TOP_RIGHT, MID_RIGHT, LOW_RIGHT)
            case 6:
                if cards[LOW_MID].color == card_color and cards[LOW_RIGHT].color == card_color:
                    self.drop_line(LOW_LEFT, LOW_MID, LOW_RIGHT)
                elif cards[TOP_LEFT].color == card_color and cards[MID_LEFT].color == card_color:
                    self.drop_line(TOP_LEFT, MID_LEFT, LOW_LEFT)
                elif cards[CENTER].color == card_color and cards[TOP_RIGHT].color == card_color:
                    self.drop_line(LOW_LEFT, CENTER, TOP_RIGHT, diagonal=True)
            case 7:
                if cards[LOW_LEFT].color == card_color and cards[LOW_RIGHT].color == card_color:
                    self.drop_line(LOW_LEFT, LOW_MID, LOW_RIGHT)
                elif cards[TOP_MID].color == card_color and cards[CENTER].color == card_color:
                    self.drop_line(TOP_MID, CENTER, LOW_MID)
            case 8:
                if cards[LOW_LEFT].color == card_color and cards[LOW_MID].color == card_color:
                    self.drop_line(LOW_LEFT, LOW_MID, LOW_RIGHT)
                elif cards[TOP_RIGHT].color == card_color and cards[MID_RIGHT].color == card_color:
                    self.drop_line(TOP_RIGHT, MID_RIGHT, LOW_RIGHT)
                elif cards[TOP_LEFT].color == card_color and cards[CENTER].color == card_color:
                    self.drop_line(TOP_LEFT, CENTER, LOW_RIGHT, diagonal=True)

    def drop_line(self, card1_pos, card2_pos, card3_pos, diagonal=False):
        cards = self.player_cards[self.current_player]
        dummy_card = Card(0, DUMMY_COLOR, True)
        if diagonal:
            if card1_pos == TOP_LEFT:
                cards[TOP_LEFT] = dummy_card
                cards[CENTER] = cards[TOP_MID]
                cards[TOP_MID] = dummy_card
                cards[LOW_RIGHT] = cards[MID_RIGHT]
                cards[MID_RIGHT] = cards[TOP_RIGHT]
                cards[TOP_RIGHT] = dummy_card
            else:
                cards[TOP_RIGHT] = dummy_card
                cards[CENTER] = cards[TOP_MID]
                cards[TOP_MID] = dummy_card
                cards[LOW_LEFT] = cards[MID_LEFT]
                cards[MID_LEFT] = cards[TOP_LEFT]
                cards[TOP_LEFT] = dummy_card
        else:
            cards[card1_pos] = dummy_card
            cards[card2_pos] = dummy_card
            cards[card3_pos] = dummy_card

    def end_turn(self):
        self.current_player = (self.current_player + 1) % self.num_players

