import pygame, sys
from settings import Settings

class SidewayShooter:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Sideway Shooter")
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            pygame.display.flip()            


if __name__ == '__main__':
    ss = SidewayShooter()
    ss.run_game()
        