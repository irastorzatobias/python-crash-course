import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    
 # Dark grey bullets
    def __init__(self,ai):
        super().__init__()
        self.screen = ai.screen
        self.settings = Settings()
        self.color = self.settings.bullet_color 
        
    # Bullet rect at (0,0)
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)

        self.rect.midtop = ai.ship.rect.midtop
    # Store the bullet position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """" Move the bullet up to the screen """

        self.y -= self.settings.bullet_speed
        
        # Update rect position
        
        self.rect.y = self.y
    
    def draw_bullet(self):
        """ Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
 