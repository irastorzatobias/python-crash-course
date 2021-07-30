import pygame

class Watch:
    def __init__(self, bs):
        # Blue screen sizes
        self.screen = bs.screen
        self.screen_rect = bs.screen.get_rect()
        
        # Image
        
        self.image = pygame.image.load('./images/watch.jpg')
        self.image = pygame.transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)