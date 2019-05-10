'''
Class name: rivard
Date: 3/23/15
Description: the objects of this class contain the information about the game such as the current page that is shown
'''
import pygame
from restart_buttons import restart_buttons 

class game():
    
    '''
    Constructer method
    Parameter:
      page - string - the name of the page shown
    '''
    def __init__(self, page):
        self.page = page
        self.score = 0
        self.score_achieved = ""
        
    '''
    Method name: game_over_check
    Parameters:
      life - life object
      mr_rivard - rivard object
      restart_p - restart button object
    Description: checks whether there is still life left, if not then reset the game
    '''
    def game_over_check(self, life, mr_rivard, path, restart_p):
        if life.life_left == 0: #check whether there is life left
            self.score_achieved = str(self.score)   #save the score before reseting the game score to 0 for the new game
            restart_p.is_clicked(mr_rivard, path, self, life) #call a function that will reset all the information so one can replay the game
            self.page = "gameover" #set the page to gameover to show the score
            
    '''
    Method name: reset
    Parameters:
      page - string - the current page shown
    Description: reset the score to 0 and redirect the user to another page
    '''    
    def reset(self, page):
        self.page = page
        self.score = 0