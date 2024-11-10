import gymnasium as gym

from game import Game


class EnvHiLoSinglePlayer(gym.Env):
    def __init__(self):
        self.game = None

    def step(self, action):
        pass

    def reset(self, seed=None, options=None):
        self.game = Game()

    def render(self):
        pass

    def close(self):
        pass
