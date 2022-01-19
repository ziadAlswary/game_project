

import mazes
import os
import keyboard  # using module keyboard
from time import sleep
import winsound
import pyfiglet

#global vairables
Level = 1
maze = mazes.maze_patterns
maze_array = maze[0][0]
pointer_r = maze[0][1] # r -> row
pointer_c = maze[0][2] # c -> col
win = False
loop = True

def set_level(L):
    global Level,maze_array,pointer_r,pointer_c,win
    Level = L
    maze_array = maze[L-1][0]
    pointer_r = maze[L-1][1] 
    pointer_c = maze[L-1][2] 
    win = False

def print_maze():
    global maze_array, pointer_r, pointer_c, Level
    print("\nLevel     :",Level)
    print("Left time : 00:00\n")
    for row in range(len(maze_array)):
        for col in range(len(maze_array[row])):
            if(row == pointer_r and col == pointer_c):
                print("o",end="")
            else:
                print(maze_array[row][col],end="")
        print()
    
    print("\n"," press ESC to exit ".center(50))

def cs():
    _ = os.system('cls')

def up():
    global pointer_r,pointer_c
    pointer_r -= 1
    if maze_array[pointer_r][pointer_c] == "@" :
        winsound.Beep(800,200)
        pointer_r += 1
def down():
    global pointer_r,pointer_c
    pointer_r += 1
    if maze_array[pointer_r][pointer_c] == "@" :
        winsound.Beep(800,200)
        pointer_r -= 1

def left():
    global pointer_r,pointer_c
    pointer_c -= 1
    if maze_array[pointer_r][pointer_c] == "@" or pointer_c == -1  :
        winsound.Beep(800,200)
        pointer_c += 1

def right():
    global pointer_r,pointer_c,win
    pointer_c += 1
    if maze_array[pointer_r][pointer_c] == ">"  :
        win = True
    elif maze_array[pointer_r][pointer_c] == "@"  :
        pointer_c -= 1
        winsound.Beep(800,200)

def get_input():
    global pointer_r,pointer_c,loop
    key = keyboard.read_key()
    
    if key == "up" : # move the player up
        up()
    elif key == "down" : # move the player down
        down()
    elif key == "left" : # move the player left
        left()
    elif key == "right" : # move the player right
        right()
    elif key == "esc": # exit from the game
        loop = False
    
def start_game():
    global win
    while loop:
        cs()
        print_maze()
        get_input()
        if win:
            if Level == 1 :
                set_level(2)
            elif Level == 2 :
                break
        sleep(.2)

    if win:
        cs()
        print("\nyou win :)\n\n")
    else:
        cs()
        print("\nyou lose :(\n\n")
def game_menu():
    cs()
    result = pyfiglet.figlet_format("M A Z E", font = "5lineoblique" )
    print(result)
    print("  MENU  ".center(50,"_"),"\n")
    print("\t1- Strart the game\n\t2- Exit")
    op = input("\t\t\nChoose : ")
    while op not in ["1","2"]:
        op = input("\t\tRe-choose : ")
    if op == "2":
        cs()
        bay_msg = pyfiglet.figlet_format("GOODBYE", font = "slant" )
        print(bay_msg)
        sleep(3)
        exit()
    else:
        start_game()

while 1:
    game_menu()


