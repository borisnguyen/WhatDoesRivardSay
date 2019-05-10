'''
Class name: rivard
Date: 4/4/15
Description: Contains the hearts and players life information
'''
import pygame

class life():
    life_left=3 #shows how many life left
    
    '''
    Constructor method
    Parameter:
      x, y - int - coordinates of the heart icon
      size - int - size of the heart icon
      pink - string - location address of pink heart
      grey - string - location address of grey heart
      num - int - the number of the heart
    '''
    def __init__(self, x, y, size, pink, grey, num):
        self.x = x
        self.y = y
        self.size = size
        self.num = num
        self.grey_heart = pygame.image.load(str(grey))
        self.pink_heart = pygame.image.load(str(pink))    
        
    '''
    Method name: draw_life
    Parameter:
      screen - pygame display
    Description: draw grey/pink hearts depending on how many lives left
    '''
    def draw_life(self, screen):
        if life.life_left>=self.num:
            screen.blit(self.pink_heart, (self.x, self.y))
        else:
            screen.blit(self.grey_heart, (self.x, self.y))