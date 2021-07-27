import pygame

class Rocket:
    def __init__(self,rg):
        # Screen settings
        self.screen = rg.screen
        self.screen_rect = rg.screen.get_rect()
        self.settings = rg.settings
    
        # Movement flags
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Load rocket image
        
        self.image = pygame.image.load('ship.bmp') # load image
        self.rect = self.image.get_rect() # get the rect of the image
        
        # Start new rocket center of the screen
        
        self.rect.center = self.screen_rect.center 
    
        # Decimal, vertical and horizontal position 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

            
        

    
    def update(self):
        """ Update rocket position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed 
               
        # update reck object
        
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """ Draw rocket at current position"""
        self.screen.blit(self.image, self.rect)
        
            
        
    