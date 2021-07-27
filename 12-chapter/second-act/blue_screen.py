import pygame
import sys

class BlueScreen:
    def __init__(self):
        pygame.init()
       
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #self.screen.width = self.screen.get_rect().width
        #self.screen.height = self.screen.get_rect().height
        pygame.display.set_caption('Blue test')

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def run(self):
        while True:
            self._check_event()
            self.screen.fill('pink')
            pygame.display.flip()


if __name__ == '__main__':
    bs = BlueScreen()
    bs.run()