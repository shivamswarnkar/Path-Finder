'''
Game: Find Path
File: Char.py
Programmer: Shivam Swarnkar
Purpose: This file contains functions which draw objects on the screen. There are several objects
such as hero, enemy and goal.
'''

import pygame
  
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

#hero
def draw_Ankur(screen, x, y):
    # Head
    pygame.draw.circle(screen, BLACK, [5+x, 5+y], 3, 1)

  
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
  
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
  
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

    #Sword
    pygame.draw.line(screen, BLACK,[9+x, 17+y], [13+x, 7+y], 2)

#enemy
def draw_Rahul(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, GREEN, [1 + x, y, 10, 10], 0)
  
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
  
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
  
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


def draw_Sheela(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, RED, [1 + x, y, 10, 10], 0)
  
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
  
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
  
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

#obsticals     
def draw_obsR(screen, x, y):
    pygame.draw.polygon(screen, RED, [[x+10,y+10],[x+20,y+20],[x+20,y]], 2)

def draw_obsB(screen, x, y):
    pygame.draw.polygon(screen, BLACK, [[x+10,y+10],[x+20,y+20],[x+20,y]], 2)

def draw_obsG(screen, x, y):
    pygame.draw.polygon(screen, GREEN, [[x+10,y+10],[x+20,y+20],[x+20,y]], 2)

#goal

def draw_goal(screen, x, y):
    pygame.draw.circle(screen, RED, [x+30,y+30], 5,1)
    pygame.draw.polygon(screen, GREEN, [[x+20,y+40],[x+40,y+40],[x+30,y+30]], 2)

