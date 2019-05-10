'''
Class Name: select_path
Date: 3/30/15
Description: This class is for the path selection frame, which is used by the player to choose from what place to shoot the electricity.
'''
import pygame

class select_path():
    
    #Different locations of the paths
    #In this dictionary the key represents the number of the path and the value is the x-coordinate (all paths have the same y-coordinate)
    path_start={
    1: -6,
    2: 22,
    3: 48,
    4: 75,
    5: 102,
    6: 129,
    7: 156,
    8: 184,
    9: 210,
    10: 237,
    11: 264,
    12: 291,
    13: 319,
    14: 346,
    15: 374,
    16: 400
    }
    
    '''
    Constructer method
    Parameter:
      frame_icon - loaded image
    '''
    def __init__(self, frame_icon):
        self.location = 1   #Whenever a path selection frame object is initialized, it's original location will be on the path#1
        self.frame_icon = frame_icon    #The icon of the path selection frame
    
    '''
    Method Name: reset()
    Description: when a new game is started, the location of the path selection frame is set to 1
    '''    
    def reset(self):
        self.location = 1
        
    '''
    Method Name: draw_path_frame
    Parameter:
      screen - pygame display
    Description: draw the path selection frame at specific coordinates
    '''        
    def draw_path_frame(self, screen):
        screen.blit(self.frame_icon, (select_path.path_start[self.location], 498))
    
    '''
    Method Name: draw_path_frame
    Parameter:
        direction - string - tells which way to move the path selection frame
    Description: move the path selection frame to the left/right path.
    '''       
    def move(self, direction):
        if direction == "K_LEFT" and self.location!=1:
            self.location = self.location - 1
        elif direction == "K_RIGHT" and self.location!=16:
            self.location = self.location + 1    