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
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        """This is a helper method, helper methods run in classes
        but aren't meant to be called through an instance"""
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        """ Update images on the screen """
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
