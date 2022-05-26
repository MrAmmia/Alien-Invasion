import pygame
from random import *
random_number = randint(-10,10)
class Star():

    def __init__(self,ai_settings, screen):
        #initialize the star in starting position
        self.screen = screen
        self.ai_settings = ai_settings
        #load star and get its rect
        self.image = pygame.image.load("images/star2.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        for i in range(100):
            self.center = self.center + random_number
            self.rect.bottom = self.rect.bottom + random_number
            self.screen.blit(self.image,self.rect)


        #Start each new ship at the bottom center of the screen
        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.top = self.screen_rect.top

        #Store a decimal value for the ships's center.
        #

    
       
    
        


    def blitme(self):
        #Draw the ship at its current location.
        self.screen.blit(self.image,self.rect)
