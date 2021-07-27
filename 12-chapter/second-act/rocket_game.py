import pygame
import sys

from settings import Settings
from rocket import Rocket

class RocketGame:
    def __init__(self):
        pygame.init()   
        # Screen settings
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        pygame.display.set_caption('Move rocket')   
        self.rocket = Rocket(self)
        
        
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    
    def _check_keyup_events(self,event):        
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    
    
            
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        
        pygame.display.flip()
        
        
    def run(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            


if __name__ == '__main__':
    rg = RocketGame()
    rg.run()
        
            