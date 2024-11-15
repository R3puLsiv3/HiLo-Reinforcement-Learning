import gymnasium as gym
import numpy as np

from .game import (Game, TOP_LEFT, TOP_MID, TOP_RIGHT, MID_LEFT, CENTER, MID_RIGHT, LOW_LEFT, LOW_MID, LOW_RIGHT,
                   CARDS_PER_PLAYER)
from .gameGUI import GameGUI


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
    metadata = {"render_modes": ["human"]}

    def __init__(self, render_mode=None, num_players=2):
        self.render_mode = render_mode
        self.game_gui = None
        self.game = Game(num_players)
        self.card = None

        # The agent can choose to swap the current card with one of the player cards or discard it.
        self.action_space = gym.spaces.Discrete(CARDS_PER_PLAYER + 1)
        # The agent observes all the player cards.
        # TODO: Add more information the observation space
        self.observation_space = gym.spaces.Discrete(CARDS_PER_PLAYER * self.game.num_players)

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

        if self.render_mode == "human":
            self.render()

    def reset(self, seed=None, options=None):
        # TODO: Select next card

        if self.render_mode == "human":
            self.game_gui = GameGUI()
        return np.asarray([card for player in self.game.player_cards for card in player]), {}

    def render(self):
        pass

    def close(self):
        pass
