#!python3
"""
Create a function to check the winner in a Tic Tac Toe game.
Game data is stored in a list:
[0,0,0,0,0,0,0,0,0,0]

The index shows the position of the X's and O's in the following gameboard
using the references:
Position 0 is always empty, to help the numbering start at 1

123
456
789

So [0,"X",0,"O",0,"X",0,0,"X","O"]
would correspond to:
X.O
.X.
.XO


Create a function called winner(game) that receives the entire list as an
input parameter. It's return value is either:
0 (no winner)
"X" (X is a winner)
"O" (O is a winner)

"""
def win(n):
    if n == b[0] and n== b[1]  and n ==b[2] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[3]  and n== b[4] and n == b[5] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[6]  and n== b[7]  and n == b[8]:
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[0] and n== b[3] and n ==b[6]:
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[1]  and n== b[4]  and n ==b[7] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[2]  and n== b[5]  and n ==b[8] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[0]  and n== b[4]  and n ==b[8] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[2]  and n== b[4]  and n ==b[6] :
        print(n,"Has won the game")
        winner = True
        return winner

"""
#!python3
b = ["1","2","3","4","5","6","7","8","9"]
winner = False
def board():
    import os
    os.system("cls")
    print(b[0]+b[1]+b[2]+ "\n" + b[3]+b[4]+b[5] + "\n"+b[6]+b[7]+b[8])

def turns():
    t=0
    while t < 9:
        turn1=""
        turn2=""
        while turn1 != "over":
            m = int(input("It is x's turn \n where do you want your x "))
            if b[m-1] == "o":
                print("sorry that spot is taken")
            else:
                b[m-1]= "x"
                turn1 = "over"
                board()
                t+=1
        if win("x")==True:
            break
        if t== 9:
            print("Nobody wins you all suck")
            break
        while turn2 != "over":
            m = int(input("It is o's turn \n where do you want your o "))
            if b[m-1] == "x":
                print("sorry that spot is taken")
            else:
                b[m-1]= "o"
                turn2 = "over"
                board()
                t+=1
        if win("o")==True:
            break
       
def win(n):
    if n == b[0] and n== b[1]  and n ==b[2] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[3]  and n== b[4] and n == b[5] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[6]  and n== b[7]  and n == b[8]:
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[0] and n== b[3] and n ==b[6]:
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[1]  and n== b[4]  and n ==b[7] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[2]  and n== b[5]  and n ==b[8] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[0]  and n== b[4]  and n ==b[8] :
        print(n,"Has won the game")
        winner = True
        return winner
    elif n == b[2]  and n== b[4]  and n ==b[6] :
        print(n,"Has won the game")
        winner = True
        return winner



board()
turns()
"""