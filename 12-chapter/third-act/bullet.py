import pygame
from pygame.sprite import Sprite



class Bullet(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.color = self.settings.bullet_color
        
        # Rect at 0,0 with width and height of the bullet, and then set the right position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ss_game.ship.rect.midright
        
        self.x = float(self.rect.x)
        
    def update(self):
        """ Move bullet across the screen"""
        # Update decimal position of the bullet
        self.x += self.settings.bullet_speed
        # Update rect position
        self.rect.x = self.x
            
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
            