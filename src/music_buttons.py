'''
Class name: music_buttons
Date: 3/25/15
Description: a subclass for music buttons that can be either turned on or off
'''
import pygame
from buttons import buttons

class music_buttons(buttons):
    music_status = "on"  
    
    '''
    Constructor
    Parameters:
      x - int - x-coordinate
      y - int - y-coordinate
      size - int - size of the icon
      white - array of strings - white button icon location address
      red - array of strings - red button icon location address
      page - string - page at which this button is shown
      redirect - string - to which page redirect the player once the button is clicked
    Description: The music button to turn on/off.
    '''
    def __init__(self, x, y, size, white, red, page, redirect):
        buttons.__init__(self, x, y, size, white[0], red[0], page, redirect)    #Inherit from parent class
        self.white_on = white[0]    #white music button when music is on 
        self.white_off = white[1]   #white music button when music is off
        self.red_on = red[0]    #red music button when music is on
        self.red_off = red[1]   #red music button when music is off
        
    '''
    Method name: is_clicked
    Describtion: Change the button icon when it is clicked in order to show the player the status of the music
    '''
    def is_clicked(self):
        if music_buttons.music_status == "off": #Change the music from off to on and show the appropriate buttons
            music_buttons.music_status = "on"
            self.white_button = pygame.image.load(self.white_on)
            self.red_button = pygame.image.load(self.red_on)
        elif music_buttons.music_status == "on":#Change the music from on to off and show the appropriate buttons
            music_buttons.music_status = "off"
            self.white_button = pygame.image.load(self.white_off)
            self.red_button = pygame.image.load(self.red_off)        