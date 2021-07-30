import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    def __init__(self):
        """ Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings() # instancia de settings, asi, si tengo que modificar algo, lo hago desde el archivo settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # setting up height, and width
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self) # create ship
        # bullets
        self.bullets = pygame.sprite.Group()
                                                                                                                                                                                                                                
        
        
        pygame.display.set_caption("Alien Invasion") # title of game
        
    def _check_events(self):
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        # Respond to keypresses
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q: # Q to quit.¿
                sys.exit() 
            elif event.key == pygame.K_SPACE: # space to shoot bullets
                self._fire_bullet()
    
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets gropu in line 19"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_keyup_events(self,event):
        # Respond to key releases
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) # changes color
        self.ship.blitme() # display ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip() # refreshes screen 

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            # Redraw the screen during each pass through the loop to, refresca color cada loop
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            self._update_screen()
                    

            

if __name__ == '__main__':
    # Make a game instance, and run the game

    ai = AlienInvasion()
    ai.run_game()