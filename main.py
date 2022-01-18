

import mazes
import os
import keyboard  # using module keyboard
from time import sleep
Level = 1
pointer_r = 1 # r -> row
pointer_c = 0 # c -> col

def print_maze(maze):
    global pointer_r
    global pointer_c
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if(row == pointer_r and col == pointer_c):
                print("+",end="")
            else:
                print(maze[row][col],end="")
        print()
    
    # print("p_row = ",pointer_r)
    # print("p_col = ",pointer_c)

def cs():
    _ = os.system('cls')

while 1:
    cs()
    print_maze(mazes.maze1)
    key = keyboard.read_key()
    if key == "up" : # move the player up
        pointer_r -= 1
    elif key == "down" : # move the player down
        pointer_r += 1
    elif key == "left" : # move the player left
        pointer_c -= 1
    elif key == "right" : # move the player right
        pointer_c += 1
    elif key == "esc": # exit from the game
        exit()
    sleep(.2)
    


