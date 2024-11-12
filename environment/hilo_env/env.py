import gymnasium as gym

from game import Game, TOP_LEFT, TOP_MID, TOP_RIGHT, MID_LEFT, CENTER, MID_RIGHT, LOW_LEFT, LOW_MID, LOW_RIGHT


class Actions:
    SWAP_TOP_LEFT = 0
    SWAP_TOP_MID = 1
    SWAP_TOP_RIGHT = 2
    SWAP_MID_LEFT = 3
    SWAP_CENTER = 4
    SWAP_MID_RIGHT = 5
    SWAP_LOW_LEFT = 6
    SWAP_LOW_MID = 7
    SWAP_LOW_RIGHT = 8
    DISCARD = 9


class EnvHiLoSinglePlayer(gym.Env):
    def __init__(self):
        self.game = None
        self.card = None

    def step(self, action):
        match action:
            case Actions.SWAP_TOP_LEFT:
                self.game.swap_cards(self.card, TOP_LEFT)
            case Actions.SWAP_TOP_MID:
                self.game.swap_cards(self.card, TOP_MID)
            case Actions.SWAP_TOP_RIGHT:
                self.game.swap_cards(self.card, TOP_RIGHT)
            case Actions.SWAP_MID_LEFT:
                self.game.swap_cards(self.card, MID_LEFT)
            case Actions.SWAP_CENTER:
                self.game.swap_cards(self.card, CENTER)
            case Actions.SWAP_MID_RIGHT:
                self.game.swap_cards(self.card, MID_RIGHT)
            case Actions.SWAP_LOW_LEFT:
                self.game.swap_cards(self.card, LOW_LEFT)
            case Actions.SWAP_LOW_MID:
                self.game.swap_cards(self.card, LOW_MID)
            case Actions.SWAP_LOW_RIGHT:
                self.game.swap_cards(self.card, LOW_RIGHT)
            case Actions.DISCARD:
                self.game.deck.discard_card(self.card)

        self.game.end_turn()
        # TODO: Select next card

    def reset(self, seed=None, options=None):
        self.game = Game()
        # TODO: Select next card

    def render(self):
        pass

    def close(self):
        pass
