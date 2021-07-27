import pygame

class Warrior:
    
    def __init__(self, bs):
        self.screen = bs.screen
        self.screen_rect = bs.screen.get_rect() # cuadrado 
        
        self.image = pygame.image.load('./warrior.bmp')
        self.image = pygame.transform.scale(self.image, (200,200)) # reescaling img 
        self.rect = self.image.get_rect() # cuadrado de la imagen
        
        # Warrior at center
        
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    
    