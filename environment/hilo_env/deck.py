
from random import shuffle

DUMMY_COLOR = -1
LIGHT_GREEN = 0
DARK_GREEN = 1
LIGHT_BLUE = 2
DARK_BLUE = 3
RED = 4
ORANGE = 5
YELLOW = 6
PURPLE = 7


class Deck:
    def __init__(self, values=range(-1, 12), num_colors=8):
        self.draw_pile = [Card(value, color) for value in values for color in range(num_colors)]
        self.discarded_card = None
        self.draw_pile_sum = sum(values) * num_colors
        self.draw_pile_size = len(self.draw_pile)

    def shuffle_draw_pile(self):
        shuffle(self.draw_pile)

    def mean(self):
        return self.draw_pile_sum / self.draw_pile_size

    def pick_draw_pile_card(self):
        card = self.draw_pile.pop()
        card.shown = True
        self.draw_pile_sum -= card.value
        self.draw_pile_size -= 1
        return card

    def pick_discarded_card(self):
        return self.discarded_card

    def discard_card(self, card):
        self.discarded_card = card

    def initialize(self):
        self.discard_card(self.pick_draw_pile_card())


class Card:
    def __init__(self, value, color, shown=False):
        self.value = value
        self.color = color
        self.shown = shown

    def show(self):
        self.shown = True
