'''
Class Name: electricity
Date: 3/31/15
Description: This class is needed for electricity that is shot in order to hit the character.
'''
from life import life

class electricity():
    exist = False   #shows whether electricity exists or not
    
    '''
    The coordinates of the points where the path changes its direction
    The list consists the number of the path, points in this path, x and y coordinates of that point
    '''
    trajectory = [
    [[1, 502], [1, 350], [15, 350], [15, 96], [1, 96]],
    [[31, 502]],
    [[56, 502], [56, 180], [42, 180], [42, 158], [56, 158]],
    [[84, 502], [84, 372], [100, 372], [100, 234], [84, 234]],
    [[112, 502]],
    [[138, 502], [138, 444], [124, 444], [124, 118], [138, 118]],
    [[166, 502], [166, 440], [152, 440], [152, 392], [164, 392]],
    [[192, 502]],
    [[220, 502], [220, 334], [204, 334], [204, 170], [220, 170]],
    [[246, 502]],
    [[272, 502], [272, 242], [254, 242], [254, 146], [272, 146]],
    [[300, 502], [300, 404], [312, 404], [312, 330], [300, 330]],
    [[328, 502]],
    [[356, 502], [356, 306], [340, 306], [340, 234], [356, 234]],
    [[384, 502]],
    [[408, 502], [408, 180], [396, 180], [396, 134], [408, 134]],
    ]
        
    #The constructor method, creates an electricity object
    def __init__(self, location, icon):
        electricity.exist = True    #Since electricity exists now, change the status of electricity.exist
        self.location = location    #The number of the path chosen by the user, when the spacebar was clicked
        
        #set the coordinate to the coordinates of a specific path, which is calculated using the location of the path selection frame, and take the y-value from the next index.  
        self.x = electricity.trajectory[self.location-1][0][0]
        self.y = electricity.trajectory[self.location-1][0][1]
        
        #number of direction_change on that path + 1 (start point)
        self.num_direction_change = len(electricity.trajectory[self.location-1])
        
        #counter is used to calculate the number of direction change done
        self.counter = 0
        
        #the electricity icon
        self.icon = icon
        
    '''
    Method name: collide_check
    Parameters:
      game_info - game object - contains the score information
      mr_rivard - rivard object - contains the coordinates of the character
    Description: Collision between two circles check
    '''
    def collide_check(self, game_info, mr_rivard):
        if (mr_rivard.x+57-self.x-20)**2+(mr_rivard.y+57-self.y-20)**2<77**2:   #Check whether two circles collide using the formula of vectors between two points and the fact that when the sum of the two radiuses is less than the distance between their centers, then they collide.
            electricity.exist=False #set to false, so electricity does not exist on the screen until electricity.exist is True again
            game_info.score+=(450-mr_rivard.y+57)//45   #Calculate the points. The main character moves in a square 450*450. The points are based on the center y-value. At top, one can get 10, at the bottom one can get 0. The higher the character, the more points one gets.
            mr_rivard.is_hit()  #Call a procedure that calculates the number of hits
            
    '''
    Method name: move
    Parameters:
      screen - pygame display
    Description: Moves the electricity on the path
    '''
    def move(self, screen):
        if self.num_direction_change == 1: #no direction changes 
            self.y=self.y-2
        elif self.x==electricity.trajectory[self.location-1][self.counter+1][0] and self.y==electricity.trajectory[self.location-1][self.counter+1][1] and self.counter+2 < self.num_direction_change:  #Its a direction change point
            self.counter+=1          
        elif self.x==electricity.trajectory[self.location-1][self.counter+1][0]:    #Go up until it meets the direction change point
            self.y=self.y-2
        elif self.y==electricity.trajectory[self.location-1][self.counter+1][1]:
            if self.x<electricity.trajectory[self.location-1][self.counter+1][0]:   #Go to right until it meets the direction change point to go up
                self.x=self.x+2
            elif self.x>electricity.trajectory[self.location-1][self.counter+1][0]: #Go to left until it meets the direction change point to go up
                self.x=self.x-2
        if self.y==58:  #Set exist to False since the electricity did not collide with the character and lose a life for that
            life.life_left-=1
            electricity.exist=False
        screen.blit(self.icon, (self.x, self.y))    #Draw the star
    