import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    """A class to manage lives the player has left."""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/png/UI/playerLife2_orange.png")
        self.rect = self.image.get_rect()