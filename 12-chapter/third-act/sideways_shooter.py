import pygame, sys

from settings import Settings
from ship import Ship
from bullet import Bullet


class SidewayShooter:
    def __init__(self):
        pygame.init()
        # Screen settings
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Sideway Shooter")
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullets(self):
        """ Creates a new bullet and adds it to the group of bullet sprite"""
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet)
            
    # Here we update element's positions
    def _update_bullets(self):
        self.bullets.update() # update bullets x,y 
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
            
    # Refresh the screen 
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()
    
    def run_game(self):
       while True:
            self._check_events()
            self.ship.update() # update ship x,y 
            self._update_bullets()
            self._update_screen()    


if __name__ == '__main__':
    ss = SidewayShooter()
    ss.run_game()
        