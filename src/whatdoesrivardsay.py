'''
Title: What does Rivard say?
Author: Boris Nguyen and Lina Zhu
Date: April 8, 2015
Description: This is a game, where the aim is to hit the main character with "electricity". This game was made hard on purpose: the main character is moving randomly, the electricity is moving slowly, there can be one electricity at a time and electricity star follows a specific path. For more information, please, read the user manual.
Known Issues: The sound does not work. Therefore, the sound button does not actually turn on/off the music. The function to allign the score in the middle was not written due to the time constraints.
'''

import sys, pygame

#Importing classes
from game import game
from life import life
from rivard import rivard
from buttons import buttons
from electricity import electricity
from select_path import select_path
from quit_buttons import quit_buttons
from music_buttons import music_buttons
from restart_buttons import restart_buttons

'''
Procedure Name: draw_buttons
Description: Draw buttons on the screen
'''
def draw_buttons():
    for button in buttons_list: #Iterate over all buttons objects
        if x>=button.x and x<=button.x+button.size and y>=button.y and y<=button.y+button.size and button.page == game_info.page:   #Check whether the mouse is over the button and if that button exists on that page, if yes then show the button with red caption, else show the button with white caption
            button.draw_red_button(screen)
        elif button.page == game_info.page: #Checks whether the button exists on that page. If yes, then show that button with white caption since the mouse is not over that button (it was check before this elif statement)
            button.draw_white_button(screen)
            
'''
Procedure Name: mouse_click
Description: Perform an action if a button was clicked
'''
def mouse_click():
    for button in buttons_list: #Iterate over all buttons objects  
            if x>=button.x and x<=button.x+button.size and y>=button.y and y<=button.y+button.size and game_info.page == button.page:   #Check whether the mouse clicked on the button and if that button exists on that page, if yes then perform an action, else do nothing since it means the mouse clicked somewhere on the screen and not on the button
                game_info.page = button.redirect    #Redirect to another page
                if button==restart_p or button==restart_go: #If the restart_buttons objects are clicked, then call a method for these buttons
                    button.is_clicked(mr_rivard, path, game_info, life) #There is a seperate if statement for these buttons since their method requires parameters compared with other buttons
                elif button!=settings_m and button!=home_s and button!=play_m and button!=home_p and button!=pause_g and button!=play_p and button!=home_go:    #If other buttons except for the home buttons, setting buttons and play buttons, call a method. The mentioned above exceptions exists because those buttons only redirect a user to another page, they do not perform an action
                    button.is_clicked() #Perform an action if a button is clicked and is not an exception
                break    #Break the loop since there is no point iterating over all elements in the array once the target button is found


'''
Procedure Name: draw_main
Description: Draw the main page
'''
def draw_main():
    screen.blit(title, (120, 110))  #Draw the title of the game
    screen.blit(adam[0], (162, 160))    #Draw the main character
    
'''
Procedure Name: draw_pause()
Description: Draw the pause page
'''
def draw_pause():
    screen.blit(large_font.render("PAUSED", 1 , (255,255,255)), (100, 200)) #Write the word "PAUSED" on screen
 
'''   
Procedure Name: draw_settings
Description: Draw the settings page
'''
def draw_settings():
    #Write "Credits" on the screen
    screen.blit(large_font.render("Credits", 1 , (255,255,255)), (100, 250))
    
    #Draw the people who made a contribution to this game
    screen.blit(adam[0], (162.5,345))
    screen.blit(lina, (300,345))
    screen.blit(boris, (20,320))
    
    #Write their names
    screen.blit(small_font.render("Boris Nguyen", 1 , (255,255,255)), (20, 470))
    screen.blit(small_font.render("Mr. Rivard", 1 , (255,255,255)), (175, 470))
    screen.blit(small_font.render("Lina Zhu", 1 , (255,255,255)), (325, 470))

'''   
Procedure Name: draw_game
Description: Draw the game
'''
def draw_game():
    path.draw_path_frame(screen)    #draw the "select path" frame
    
    for heart in hearts:    #Draw all hearts (life)
        heart.draw_life(screen)    
        
    mr_rivard.move(screen)      #Draw the character. The function is named move since everytime after running that function the coordinates of the character will change resulting in the characters movement
    
    if electricity.exist == True:     #If electricity exists then do the following code
        shoot.move(screen)      #Draw the star. The function is named move since everytime after running that function the coordinates of the star will change resulting in the star movement
        shoot.collide_check(game_info, mr_rivard)   #Check whether the star collides with the character
        game_info.game_over_check(life, mr_rivard, path, restart_p)  #Check whether all lives are gone.
    screen.blit(large_font.render(str(game_info.score), 1 , (255,255,255)), (15, 6))    #Show the score
    
'''
Procedure Name: draw_game_over
Description: Draw the game over page
'''
def draw_game_over():
    #Show the score on the screen
    screen.blit(xlarge_font.render("SCORE:", 1 , (255,255,255)), (35, 150))
    screen.blit(xlarge_font.render(str(game_info.score_achieved), 1 , (255,255,255)), (280, 150))
    
pygame.init()

#create a graphical window
size = width, height = 450, 600
screen = pygame.display.set_mode(size)

#load graphics
background = pygame.image.load("background.png")
title = pygame.image.load("title.png")
adam = [pygame.image.load("adam0.png"), pygame.image.load("adam1.png"), pygame.image.load("adam2.png"), pygame.image.load("adam3.png"), pygame.image.load("adam4.png")]
lina = pygame.image.load("lina.png")
boris = pygame.image.load("boris.png")
frame_icon = pygame.image. load("select.png")

#fonts
xlarge_font = pygame.font.Font('heav.ttf', 80)
large_font = pygame.font.Font('ComputerAmok.ttf', 60)
small_font = pygame.font.Font('heav.ttf', 20)

#create buttons class objects
#  1) buttons on the main page:
play_m = buttons(38, 375, 100, "play0.png", "play1.png", "main", "game")
quit_m = quit_buttons(313, 375, 100, "exit0.png", "exit1.png", "main", "")
settings_m = buttons(175, 375, 100, "settings0.png", "settings1.png", "main", "settings")
#  2) buttons on the setting page
home_s = buttons(260, 100, 100, "home0.png", "home1.png", "settings", "main")
music_s = music_buttons(100, 100, 100, ["musicon0.png", "musicoff0.png"], ["musicon1.png", "musicoff1.png"], "settings", "settings")
#  3) buttons on the gameplay page
pause_g = buttons(370, 6, 60, "pause0.png", "pause1.png", "game", "pause")
#  4) buttons on the pause page
play_p = buttons(38, 325, 100, "play0.png", "play1.png", "pause", "game")
home_p = buttons(313, 325, 100, "home0.png", "home1.png", "pause", "main")
restart_p = restart_buttons(175, 325, 100, "restart0.png", "restart1.png", "pause", "game")
#  5) buttons on the gamen  over page
restart_go = restart_buttons(100, 325, 100, "restart0.png", "restart1.png", "gameover", "play")
home_go = buttons(260, 325, 100, "home0.png", "home1.png", "gameover", "main")


buttons_list = [] #a list containing all button objects, this list is later used for iteration
#append the list with the button object.
buttons_list.append(play_m)
buttons_list.append(play_p)
buttons_list.append(home_s)
buttons_list.append(home_p)
buttons_list.append(quit_m)
buttons_list.append(pause_g)
buttons_list.append(music_s)
buttons_list.append(home_go)
buttons_list.append(restart_p)
buttons_list.append(restart_go)
buttons_list.append(settings_m)

#Create a list with 3 life objects. The user will have 3 users.
hearts = [life(160, 6, 60, "heart0.png","heart1.png", 1),life(230, 6, 60, "heart0.png","heart1.png", 2),life(300, 6, 60, "heart0.png","heart1.png", 3)]

#Create a list with 3 sounds representing the mood of the character
music = [pygame.mixer.Sound("sound0.wav"), pygame.mixer.Sound("sound1.wav"), pygame.mixer.Sound("sound2.wav")]

#Create a list with 2 sounds that the character does when the star does/doesn't collide with the character
sound_effects = [pygame.mixer.Sound("ouac.wav"), pygame.mixer.Sound("laugh.wav")]

#Create the game object containing the information of the game such as at which page the user is now
game_info = game("main")

#Create the character rivard
mr_rivard = rivard(adam, music, sound_effects)

#Create path frame object, which is used to select the location at which the electricity will be shot
path = select_path(frame_icon)

#Play intro music
intro = pygame.mixer.Sound("intro.wav")

#Game loop
while True:
    #Draw the background photo
    screen.blit(background, (0, 0))
    
    #Get the mouse coordinates
    x, y = pygame.mouse.get_pos()    
    
    #Depending on what page is needed to be shown, call the function that draws that page
    if game_info.page == "main":
        draw_main()
    elif game_info.page == "game":
        draw_game()
    elif game_info.page == "pause":
        draw_pause()
    elif game_info.page == "gameover":
        draw_game_over()
    elif game_info.page == "settings":
        draw_settings()    
    
    #Draw the buttons
    draw_buttons()
    
    #If an event occurs
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #The red cross button is clicked, the window close
            #Quits the game
            pygame.display.quit()
            sys.exit()    
        elif event.type == pygame.MOUSEBUTTONDOWN:  #The mouse button is clicked
            mouse_click() #Check if it was clicked on a button. If yes, then perform an action.
        elif event.type == pygame.KEYDOWN:  #A key is pressed
            if event.key == pygame.K_RIGHT  and game_info.page=="game":         #Check if the right key was hit and if it is the game itself because in the game, right is responsible for moving the path selection frame to the right
                path.move("K_RIGHT")                                            #Move the path selection frame
            elif event.key == pygame.K_LEFT and game_info.page=="game":         #Check if the left key was hit and if it is the game itself because in the game, left is responsible for moving the path selection frame to the left
                path.move("K_LEFT")                                             #Move the path selection frame
            elif event.key == pygame.K_SPACE and game_info.page=="game":        #Check if the spacebar was hit and if it is the game itself because in the game, spacebar is responsible for shooting
                if electricity.exist == False:                                  #Shoot electricity only when other electricity does not exist. This is made in order to make the game more complicated since when the character is at the bottom, a user can press the spacebar many times and get many scores
                    shoot = electricity(path.location, pygame.image.load("star.png"))
    
    #Flip the screen that has the drawings with the screen that is shown to the user
    pygame.display.flip()    