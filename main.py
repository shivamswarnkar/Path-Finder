'''
--------------------------------------------------------------------------------
Game Designer Name: Shivam Swarnkar
Comment:
For instructions, read "Read.txt" in base folder
Music of This game does not belong to Programmar
For the copy right related matters, read "Readme.txt" file
base folder.

--------------------------------------------------------------------------------
'''

'''
--------------------------------------------------------------------------------
Info On Game Design: (Read before you play the game)

All moving objects are not real, most of them are fake to make player
uncomfortable, means you will not always loose life if you touch an object.
Also, there is a part in game where you will also loose life if any strong
enemy pass through you.

In addition, use arrow keys to move, and keep watching timer on the top right
of the screen. If time ends then you will loose the game.

To win the game, place the head of the player ( means player on the scree) at
the center of the goal. 
--------------------------------------------------------------------------------
'''

import pygame
import game


def main():
    done = False
    while not done :
        done = game.play()


main()

