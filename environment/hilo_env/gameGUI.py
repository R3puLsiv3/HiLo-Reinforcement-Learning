import pygame
import sys

from pygame.locals import QUIT


class GameGUI:
    def __init__(self):
        self.running = True

        pygame.init()
        window = pygame.display.set_mode((400, 600), pygame.RESIZABLE)
        pygame.display.set_caption("HiLo")

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            window.fill((0, 0, 0))
            pygame.display.update()
