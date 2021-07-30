import pygame, sys

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Printing keys')
   
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                else:
                    print(event.key)
    def run(self):
        while True:
            self._check_events()
            self.screen.fill('red')
            pygame.display.flip()


if __name__ == '__main__':
    ks = Keys()
    ks.run()