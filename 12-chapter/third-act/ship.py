import pygame

from sideways_shooter import SidewayShooter
from settings import Settings
class Ship:
    def __init__(self,ss_game):
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        # Settings
        self.settings = Settings()
        
        # Loading ship image         
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the left side of the screen 

        self.rect.midright = self.screen_rect.midleft
        
        self.y = float(self.rect.y)
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
        
        def update(self):
            """ Update ship position based on movement flags"""
            if self.moving_up and self.rect.top > 0:
                self.y -= self.settings.ship_speed
            if self.moving_down and self.rect.bottom < self.screen.rect.bottom:
                self.y += self.settings.ship_speed
            # Update values
            self.rect.y = self.y
        
        def blitme(self):
            """ Draw the ship at the current location"""
            pygame.blit(self.image, self.rect)
        