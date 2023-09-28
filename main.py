#this is my battle ship game
#notes

import random
ran_int = random.randint(0,10)
rows = 12
collumns = 12
print  ("    1    2    3    4    5    6    7    8    9    10   11   12")
#print ("    A    B    C    D    E    F    G    H    I    J    K    L")1
board = [["~" for i in range(collumns)]for j in range(rows)]
for i in range(0,12):
    print(i, board[i])
xinput = int(input("give me x"))
yinput = int(input("give me y"))
axis1 = input("L/R or U/D")
print("you picked "+ axis1)
def three_boat():
    if axis == "U" or axis == "D" or axis == "u" or axis == "d" or axis == "U/D":
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
    else:
        board[xinput][yinput] = "B"
        board[xinput][yinput + 1] = "B"
        board[xinput][yinput - 1] = "B"
three_boat()
#this is the three boat for game logic
def three_boat_for_gamelogic ():
    ran_dir = random.randint(0,1)
    xinput = random.randint(1,11)
    yinput = random.randint(1,11)

    if ran_dir == 1:
        if board[xinput][yinput] == "~" and board[xinput + 1][yinput] == "~" and board[xinput - 1][yinput] == "~":
            board[xinput][yinput] = "B"
            board[xinput + 1][yinput] = "B"
            board[xinput - 1][yinput] = "B"
    else:
        if board[xinput][yinput] == "~" and board[xinput][yinput + 1] == "~" and board[xinput][yinput - 1] == "~":
            board[xinput][yinput] = "B"
            board[xinput][yinput + 1] = "B"
            board[xinput][yinput - 1] = "B"
three_boat_for_gamelogic()

board = [["~" for i in range(collumns)]for j in range(rows)]
for i in range(0,12):
    print(i, board[i])
xinput = int(input("give me x"))
yinput = int(input("give me y"))
axis2 = input("L/R or U/D")
print("you picked "+ axis2)
def three_boat():
    if axis == "U" or axis == "D" or axis == "u" or axis == "d" or axis == "U/D":
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
    else:
        board[xinput][yinput] = "B"
        board[xinput][yinput + 1] = "B"
        board[xinput][yinput - 1] = "B"
three_boat()


for small_coor in range(0,3):
    ran_int = random.randint(0,12)
    board[xinput][yinput] = "B"

for i in range(0,12):
    print(i, board[i])

def pick_target_player1():
    target_x = int(input("Pick coordinates on the X axis"))
    target_y = int(input("Pick coordinates on the Y axis"))
    if board[target_x][target_y] == "B":
        print ("Direct Hit!")
        board[target_x][target_y] = "X"
    elif board [target_x][target_y] == "X" or board [target_x][target_y] == "O":
        print ("you already guessed there, you lose a turn!")
    else:
        board [target_x][target_y] = "O"
    for i in range(0, 12):
        print(i, board[i])
pick_target_player1()
def pick_target_player1():
    target_x = int(input("Pick coordinates on the X axis"))
    target_y = int(input("Pick coordinates on the Y axis"))
    if board[target_x][target_y] == "B":
        print ("Direct Hit!")
        board[target_x][target_y] = "X"
    elif board [target_x][target_y] == "X" or board [target_x][target_y] == "O":
        print ("you already guessed there, you lose a turn!")
    else:
        board [target_x][target_y] = "O"
    for i in range(0, 12):
        print(i, board[i])
pick_target_player1()





