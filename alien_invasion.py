import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game assets and behaviors"""
    def __init__ (self):
        """Initialize the game, create resources."""
        pygame.init()

        self.settings=Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
        #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

        #Redraw the screen with my color
            self.screen.fill(self.settings.bg_color)

        #Spawn player ship
            self.ship.blitme()

        # Make most recently drawn screen visible
            pygame.display.flip()

if __name__=='__main__':
    # Make a game instance and run the game
    ai= AlienInvasion()
    ai.run_game()
