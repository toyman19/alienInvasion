import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Class to manage game assets and behaviors"""

    def __init__ (self):
        """Initialize the game, create resources."""
        pygame.init()
        self.settings=Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
        #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        """This is a helper method, helper methods run in classes
        but aren't meant to be called through an instance"""
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """ Respond to key press """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """ Respond to key release """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """ Update images on the screen """
    #Redraw the screen with my color
        self.screen.fill(self.settings.bg_color)
    #Spawn player ship
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    # Make most recently drawn screen visible
        pygame.display.flip()



if __name__=='__main__':
    # Make a game instance and run the game
    ai= AlienInvasion()
    ai.run_game()
