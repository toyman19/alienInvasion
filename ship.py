import pygame

class Ship:
    """A class to manage player ship"""
    def __init__ (self, ai_game):
        """Initialize ship and it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship_small.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right= False
        self.moving_left = False



    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1





    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
