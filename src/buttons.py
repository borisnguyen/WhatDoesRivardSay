'''
Class name: buttons
Date: 3/24/15
Description: class for buttons in this game
'''
import pygame

class buttons():
    '''
    Constructor method
    Parameters:
      x, y - int - coordinates of the button
      size - int - size of the icon picture
      white - string - location address of button with white captions
      red - string - location address of button with red captions
      page - string - the page where this button appears
      redirect - string - change the page that is shown to the one in redirect
    '''
    def __init__(self, x, y, size, white, red, page, redirect):
        #coordinates and size of the button
        self.x = x
        self.y = y
        self.size = size
        self.page = page    #the page on which the button is shown
        self.white_button = pygame.image.load(white)    #load the button with white caption
        self.red_button = pygame.image.load(red)        #load the button with red caption
        self.redirect = redirect    #the page to which the game is redirected once the button is clicked
        
    '''
    Methods: draw_white_button and draw_red_button
    Parameter:
      screen - pygame display
    Describtion: draw buttons with different captions depending on the mouse position
    '''
    def draw_white_button(self, screen):    #draw the white button
        screen.blit(self.white_button, (self.x, self.y))
    def draw_red_button(self, screen):  #draw the red button
        screen.blit(self.red_button, (self.x, self.y))