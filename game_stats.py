class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Read the all-time High score from a file then assign it to high_score attribute.
        try:
            with open("all-time-high-score.txt", "r") as file:
                high_score = file.readline()
                self.high_score = int(high_score.strip())
        except Exception:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1