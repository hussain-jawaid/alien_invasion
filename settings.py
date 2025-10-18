import pygame 


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height  = 700
        self.bg_color = (0, 0, 0)
        pygame.display.set_caption("Alien Invasion")
        self.background_img = pygame.image.load("images/backgrounds/blue.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 215, 0)
        self.bullets_allowed = 3