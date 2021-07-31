import pygame

class Settings:
    def __init__(self):
        # Screen settings
        
        self.width = 800
        self.height = 600
        self.bg_color = (255,255,255)
        
        # Ship settings
        
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_color = 'red'
        self.bullet_speed = 1.5
        self.bullet_width = 60
        self.bullet_height = 15
        self.bullets_allowed = 3