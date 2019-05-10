'''
Class name: rivard
Date: 3/25/15
Description:
'''
import game
from buttons import buttons
from life import life
from rivard import rivard
from electricity import electricity
from select_path import select_path
import pygame


class restart_buttons(buttons):
    '''
    Method: is_clicked
    Parameters:
      mr_rivard - rivard object
      path - select_path object
      game_info - game object
      life - life object
    Description: resets the game so one can restart it or replay it
    '''
    def is_clicked(self, mr_rivard, path, game_info, life):
        life.life_left = 3 #set life left to 3
        mr_rivard.reset() #reset mr_rivard location, mood and speed
        path.reset() #reset the location of the path selection frame
        game_info.reset("game") #reset the game_info such as score
        electricity.exist=False #remove any existing electricity on the screen