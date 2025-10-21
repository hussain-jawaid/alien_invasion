import pygame 


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height  = 700
        self.bg_color = (0, 0, 0)
        pygame.display.set_caption("Alien Invasion")
        self.background_img = pygame.image.load("images/backgrounds/blue.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 215, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.load_sounds()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 3
        self.alien_speed = 1.5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def load_sounds(self):
        """Load the sounds for the game elements."""
        self.bullet_shoot = pygame.mixer.Sound("Bonus/sfx_laser1.ogg")
        self.ship_lose = pygame.mixer.Sound("Bonus/sfx_lose.ogg")