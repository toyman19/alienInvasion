import pygame

class Ship:
    """A class to manage player ship"""
    def __init__ (self, ai_game):
        """Initialize ship and it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship_small.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Ship movement
        # This is because x and y arguments can only accept integer
        self.x = float(self.rect.x)

        self.moving_right= False
        self.moving_left = False

    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
                self.x -= self.settings.ship_speed

        # after moinv update self.rect
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
