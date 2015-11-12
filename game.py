# This Python file uses the following encoding: utf-8
'''
Game: Find Path
File: game.py
Programmer: Shivam Swarnkar
Purpose: This file contains one function play which allows caller to run
the entire game for one time. It uses functions from the file "char.py"
'''

import pygame
import char
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)



#function play()
def play():
 
    pygame.init()

    exit_code = 0

    #plyer
    ankur_x = 20
    ankur_y = 20
    ankur_speed_x = 0
    ankur_speed_y = 0

    #scoring
    time_left = 600
    life = 3 #change the life to make game easy

    #goal
    
    r_change = 5
    b_change = 5
    g_change = 5

    rad_r = 30
    rad_b = 20
    rad_g = 50
 
    # Set the height and width of the screen
    s_x = 800
    s_y = 800
    size = [s_x, s_y]

    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Find Path")
 
    #Loop
    done = False
 
    # manage speed of the screen updates
    clock = pygame.time.Clock()
 
    # Starting position of the rectangle
    rect_x = 50
    rect_y = 50
 
    # Speed and direction of rectangle
    rect_change_x = 5
    rect_change_y = 5
 
    #fonts we use to draw text
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 72)
    font3 = pygame.font.Font(None, 14)
    font4 = pygame.font.Font(None, 20)
 
    display_instructions = True
    instruction_page = 1

    pygame.mixer.music.load('open.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    c1_r = 50
    c2_r = 25

    c1_change = 5
    c2_change = 5

    #obs

    x_ra = 130
    x_sh = 330
    y_ra = 200
    y_sh = 350
 
    # Create an empty array
    obs_listR = []
    obs_listG = []
 
    # add different x,y pair into the empy arrys
    y_g = 0
    y_r = 0
    for i in range(50):
        x_g = (s_x/4)
        y_g +=50
        obs_listG.append([x_g, y_g])

    for i in range(50):
        x_r = (3*s_x/4)
        y_r +=50
        obs_listR.append([x_r, y_r])


    # -------- Welcome Page Loop -----------
    
    while not done and display_instructions:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('open.mp3')
                pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1
                
                if instruction_page == 3:
                    display_instructions = False


        screen.fill(WHITE)
        

 
        if instruction_page == 1:
            
            text = font.render("WELCOME", True, BLACK)
            screen.blit(text, [250, 350])
 
            text = font.render("Click To Continue....", True, BLACK)
            screen.blit(text, [250, 400])
 
        if instruction_page == 2:
            text = font1.render("F", True, GREEN)
            screen.blit(text, [250, 350])

            text = font1.render("I", True, RED)
            screen.blit(text, [280, 350])

            text = font1.render("N", True, BLACK)
            screen.blit(text, [310, 350])

            text = font1.render("D", True, GREEN)
            screen.blit(text, [340, 350])

            text = font1.render("P", True, GREEN)
            screen.blit(text, [350, 400])

            text = font1.render("A", True, RED)
            screen.blit(text, [380, 400])

            text = font1.render("T", True, BLACK)
            screen.blit(text, [410, 400])

            text = font1.render("H", True, GREEN)
            screen.blit(text, [440, 400])

            text = font.render("©Shivam Swarnkar", True, BLUE)
            screen.blit(text, [500, 750])

        pygame.draw.circle(screen, GREEN, [375,375], c1_r, 2)
        pygame.draw.circle(screen, RED, [375,375], c2_r, 2)

        c1_r += c1_change

        c2_r += c2_change

        if c1_r > 400 or c1_r < 50:
            c1_change = c1_change*-1

        if c2_r >400  or c2_r < 25:
            c2_change = c2_change*-1

  
        clock.tick(60)

        pygame.display.flip()

    
    # -------- Main GAME Loop -----------
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('music.mp3')
                pygame.mixer.music.play()

            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    ankur_speed_x =- 3
                elif event.key == pygame.K_RIGHT:
                    ankur_speed_x = 3
                elif event.key == pygame.K_UP:
                   ankur_speed_y =- 3
                elif event.key == pygame.K_DOWN:
                    ankur_speed_y = 3
                  
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT:
                    ankur_speed_x =0
                elif event.key == pygame.K_RIGHT:
                    ankur_speed_x =0
                elif event.key == pygame.K_UP:
                    ankur_speed_y =0
                elif event.key == pygame.K_DOWN:
                    ankur_speed_y =0

        ankur_x += ankur_speed_x
        ankur_y += ankur_speed_y

    
     
        # Set the screen background
        screen.fill(WHITE)

        #create player position
        char.draw_Ankur(screen, ankur_x, ankur_y)

        #create goal
        char.draw_goal(screen, 700, 700)
    
        pygame.draw.circle(screen, RED, [730,740], rad_r, 2)
        pygame.draw.circle(screen, BLACK, [730,740], rad_b, 2)
        pygame.draw.circle(screen, GREEN, [730,740], rad_g, 2)

        rad_r += r_change
        rad_b += b_change
        rad_g += g_change

        if rad_r > 70 or rad_r < 30:
            r_change = r_change*-1
        if rad_b > 70 or rad_b < 20:
            b_change = b_change*-1
        if rad_g > 70 or rad_g < 30:
            g_change = g_change*-1



        #Process rahul and sheela
        char.draw_Rahul(screen, x_ra, y_ra)
        char.draw_Sheela(screen, x_sh, y_sh)
        char.draw_Rahul(screen, x_ra+random.randint(0,50), y_ra+random.randint(0,50))
        char.draw_Sheela(screen, x_sh+random.randint(0,50), y_sh+random.randint(0,50))
        char.draw_Rahul(screen, x_ra+random.randint(0,50), y_ra+random.randint(0,50))
        char.draw_Sheela(screen, x_sh+random.randint(0,50), y_sh+random.randint(0,50))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra+random.randint(0,350))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh+random.randint(0,350))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra+random.randint(0,350))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh+random.randint(0,350))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra+random.randint(0,350))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh+random.randint(0,350))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra+random.randint(0,350))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh+random.randint(0,450))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra-random.randint(0,550))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh-random.randint(0,650))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra-random.randint(0,550))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh-random.randint(0,650))
        char.draw_Rahul(screen, x_ra+random.randint(0,100), y_ra-random.randint(0,550))
        char.draw_Sheela(screen, x_sh+random.randint(0,100), y_sh-random.randint(0,650))

        x_ra_change = random.randint(0, 30)
        y_ra_change = random.randint(0, 30)
        x_sh_change = random.randint(0, 30)
        y_sh_change = random.randint(0, 30)

        x_ra += x_ra_change
        y_ra += y_ra_change
        x_sh += x_sh_change
        y_sh += y_sh_change

    


        if y_ra > 800:
                # Reset it just above the top
                y_ra = 0

        if y_sh > 800:
                # Reset it just above the top
                y_sh = 0

        if x_ra > 300:
                # Reset it just above the top
                x_ra = 130

        if x_sh > 600:
                # Reset it just above the top
                x_sh = 330

    
 
        # Process each obs  in the list
        for i in range(len(obs_listG)):
         
            # Draw the obs
            char.draw_obsR(screen, obs_listG[i][0], obs_listG[i][1])
            # Move the obs down one pixel
            obs_listG[i][1] += 2
         
            # If the obs has moved off the bottom of the screen
            if obs_listG[i][1] > 800:
                # Reset it just above the top
                y_g = 0
                obs_listG[i][1] = y_g
                # Give it a new x position
                x_g = (s_x/4)
                obs_listG[i][0] = x_g

        for i in range(len(obs_listR)):
     
            # Draw the obst
            char.draw_obsG(screen, obs_listR[i][0], obs_listR[i][1])
            # Move down
            obs_listR[i][1] += 8
         
            # If the obs has moved off the bottom of the screen
            if obs_listR[i][1] > 800:
                # Reset it just above the top
                y_r = 0
                obs_listR[i][1] = y_r
                # Give it a new x position
                x_r = (3*s_x/4)
                obs_listR[i][0] = x_r

        #game Alogrithm

        hit1 = 0
        hit2 = 0

        for i in range(len(obs_listG)):
            if (obs_listG[i][1]+10 <= ankur_y and obs_listG[i][1]+15 >= ankur_y):
                if (obs_listG[i][0]+10 <= ankur_x and obs_listG[i][0]+20 >= ankur_x):
                    hit1 = 1
        life = life-hit1

        for i in range(len(obs_listR)):
            if (obs_listR[i][1]+10 <= ankur_y and obs_listR[i][1]+15 >= ankur_y):
                if (obs_listR[i][0]+10 <= ankur_x and obs_listR[i][0]+20 >= ankur_x):
                    hit2 = 1
        life = life-hit2

        if(ankur_x < x_ra +2.5 or ankur_x > x_ra -2.5):
            if(ankur_y < y_ra +2.5 and ankur_y > y_ra -2.5):
                life = life - 1
            
        if(ankur_x < x_sh +2.5 or ankur_x > x_sh -2.5):
            if(ankur_y < y_sh +2.5 and ankur_y > y_sh -2.5):
                life = life - 1

        if(ankur_x == 725):
            if(ankur_y ==725):
                exit_code = 1
                done = True

    


        string = "Time Left: " + str(time_left)

        if time_left > 0:
            time_left = time_left -1
        elif time_left == 0:
            exit_code = -1
            done = True

        text = font3.render(string, True, RED)
        screen.blit(text, [700,20])

        if life == 0:
            exit_cod = -1
            done = True

        dist = 0

       

        string = "Lives left: " + str(life)

        text = font4.render(string, True, BLACK)
        screen.blit(text, [5, 680])

        for times in range(life):
            dist += 20
            char.draw_Ankur(screen, dist, 700)
             
        
        pygame.display.flip()
        clock.tick(20)
    
    clicked = True
    done = False

    
    #---------GAME OVER SCREEN---------------
    if exit_code == -1 or exit_code == 0:
        pygame.mixer.music.load('boo.mp3')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
        screen_counter = 0
        while not done and clicked:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
                    

                elif event.type == pygame.constants.USEREVENT:
                    pygame.mixer.music.load('music.mp3')
                    pygame.mixer.music.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = False

            if screen_counter < 5:
                screen_counter += 1

            else:
                screen_counter = 0

    
        # Set the screen background
            if(screen_counter == 1):
                screen.fill(GREEN)
            elif(screen_counter % 2 == 0):
                screen.fill(BLACK)
            else:
                screen.fill(RED)
        # Set the screen background
        

            text = font.render("GAME OVER ", True, RED)
            screen.blit(text, [250, 350])
 
            text = font.render("Click To Start From beginning ....", True, WHITE)
            screen.blit(text, [250, 400])

            text = font.render("©Shivam Swarnkar", True, WHITE)
            screen.blit(text, [500, 750])

        


            pygame.draw.circle(screen, WHITE, [375,375], c1_r, 2)
            pygame.draw.circle(screen, RED, [375,375], c2_r, 2)

            c1_r += c1_change

            c2_r += c2_change

            if c1_r > 400 or c1_r < 50:
                c1_change = c1_change*-1

            if c2_r >400  or c2_r < 25:
                c2_change = c2_change*-1

  
            clock.tick(60)

            pygame.display.flip()
    # on exit.

    
    # on exit.

    #---------Winner Screen----------------

    elif exit_code == 1:
        pygame.mixer.music.load('clap.mp3')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
        while not done and clicked:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop

                elif event.type == pygame.constants.USEREVENT:
                    pygame.mixer.music.load('open.mp3')
                    pygame.mixer.music.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = False
 
        # Set the screen background
            screen.fill(GREEN)

            text = font.render("YOU WON!!!!", True, RED)
            screen.blit(text, [250, 350])
 
            text = font.render("Click To Start From beginning ....", True, WHITE)
            screen.blit(text, [250, 400])

            text = font.render("©Shivam Swarnkar", True, WHITE)
            screen.blit(text, [500, 750])

        


            pygame.draw.circle(screen, WHITE, [375,375], c1_r, 2)
            pygame.draw.circle(screen, RED, [375,375], c2_r, 2)

            c1_r += c1_change

            c2_r += c2_change

            if c1_r > 400 or c1_r < 50:
                c1_change = c1_change*-1

            if c2_r >400  or c2_r < 25:
                c2_change = c2_change*-1

  
            clock.tick(60)

            pygame.display.flip()
        
        

    pygame.quit()

    return done



