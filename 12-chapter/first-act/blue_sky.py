import pygame
import sys

from warrior import Warrior

class BlueSky:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Blue sky")
        self.warrior = Warrior(self)
    
    def _catch_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill('blue')
        self.warrior.blitme()
        pygame.display.flip()
        
    def run_game(self):
        while True:
            self._catch_event()
            self._update_screen()
            
            

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
    