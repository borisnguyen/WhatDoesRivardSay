'''
Class Name: quit_buttons
Date: 3/25/15
Description: This is a subclass for the quit buttons that lets the user quit the game.
'''
import pygame, sys
from buttons import buttons

class quit_buttons(buttons):    #Subclass of the parent class buttons
    #Close the program
    def is_clicked(self):
        pygame.display.quit()
        sys.exit()