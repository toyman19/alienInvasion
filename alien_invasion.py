import sys

import pygame

class AlienInvasion:
    """Class to manage game assets and behaviors"""
    def __init__ (self):
        """Initialize the game, create resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #Set BG color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
        #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

        #Redraw the screen with my color
            self.screen.fill(self.bg_color)

        # Make most recently drawn screen visible
            pygame.display.flip()

if __name__=='__main__':
    # Make a game instance and run the game
    ai= AlienInvasion()
    ai.run_game()
