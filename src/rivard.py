'''
Class name: rivard
Date: 3/30/15
Description:
'''
from random import randint
import pygame

class rivard():
    speed = [2,3,3,4,4,6]   #speed for different moods
    
    x_delta = randint(-1,1) #random x change for movement direction
    y_delta = randint(-2,2) #random y change for movement direction
    while x_delta==0: #make sure that it is not 0 because then it will move vertically or will not move at all
        x_delta = randint(-1,1)
    while y_delta==0: #make sure that it is not 0 because then it will move horizontally    
        y_delta = randint(-2,2)
    #The reason why the x and y changes are random after every screen border collision is to make the game more difficult
    
    '''
    Constructor method
    Parameters:
      icon - array - different faces
      music - loaded sounds
      sound_effects - loaded sound_effects
    '''
    def __init__(self, icon, music, sound_effects):
        self.x = randint(100, 300)
        self.y = randint(174, 300)
        self.faces = icon
        self.face = icon[0]
        self.mood = 0
        self.hit_num = 0
        self.music = music
        self.sound_effects = sound_effects
        
    '''
    Method name: reset
    Description: resets the characters location, sets its face to the smiling one, resets its mood and hitting counter to 0. This is done to replay the game
    '''
    def reset(self):
        self.x = randint(100, 300)
        self.y = randint(174, 300)
        self.face = self.faces[0]       
        self.mood = 0
        self.hit_num = 0
        
    '''
    Method name: move
    Parameter: 
      screen - python display
    Description: move the character inside a square
    '''
    def move(self, screen):
        if self.x+rivard.x_delta >= 0 and self.x+125+rivard.x_delta <= 450 and self.y+ rivard.y_delta >= 74 and self.y+115+rivard.y_delta <= 524:   #if the character is inside the square and does not touch its border, than change its location by x and y delta
            self.x = self.x + rivard.x_delta
            self.y = self.y + rivard.y_delta
        else:
            if self.x+rivard.x_delta<0: #if it touches the left border, change the x delta to positive so it will move to the right
                rivard.x_delta = randint(1,rivard.speed[self.mood]) 
            elif self.x+125+rivard.x_delta>450: #if it touches the right border, change the x delta to positive so it will move to the left
                rivard.x_delta = (-1)*randint(1,rivard.speed[self.mood])
            if self.y+rivard.y_delta<74: #if it touches the top border, change the y delta to positive so it will move down
                rivard.y_delta = randint(1,rivard.speed[self.mood+1])
            elif self.y+115+rivard.y_delta>524: #if it touches the bottom border, change the y delta to positive so it will move up
                rivard.y_delta = (-1)*randint(1,rivard.speed[self.mood+1])
            
        screen.blit(self.face, (self.x, self.y))
    
    '''
    Method name: is_hit
    Description: if the character was hit 5 times, than change the mood unless it is the angriest mood already
    '''
    def is_hit(self):
        self.hit_num+=1
        if self.mood!=4 and self.hit_num == 5:
            self.mood+=1
            self.face = self.faces[self.mood]
            self.hit_num = 0