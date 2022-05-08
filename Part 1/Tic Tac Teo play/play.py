from random import randint

playboard = [[1,2,3],[4,"X",6],[7,8,9]]
FreeFeild = [(int,int)]


def DisplayBoard(board):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|   ",board[i][0],"   |   ",board[i][1],"   |   ",board[i][2],"   |",sep="")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def EnterMove(board):
    playermove = int(input("Enter Your Move: "))
    if playermove not in board:
        print("Invalid Move")
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j]==playermove:
                    board[i][j]="O"


def MakeListOfFreeFields(board):
    index = 0
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                FreeFeild[index] = (i,j)
                index = index + 1

def VictoryFor(board, sign):
    if(board[0][0] == sign and board[0][1] == sign and board[0][2]==sign ) or (board[1][0] == sign and board[1][1] == sign and board[1][2]==sign ) or (board[2][0] == sign and board[2][1] == sign and board[2][2]==sign ) or  (board[0][0] == sign and board[1][0] == sign and board[2][0]==sign ) or (board[0][1] == sign and board[1][1] == sign and board[2][1]==sign ) or (board[0][2] == sign and board[1][2] == sign and board[2][2]==sign ) or (board[0][0] == sign and board[1][1] == sign and board[2][2]==sign ) or (board[0][2] == sign and board[1][1] == sign and board[2][0]==sign ):
        if sign == "O":
            print("You won!")
        else:
            print("You lose")

def DrawMove(board):
    rand = randint(0,len(FreeFeild)-1)
    compmove = tuple(FreeFeild[rand])
    board[compmove[0]][compmove[1]] = "X"
    DisplayBoard(board)

DisplayBoard(board=playboard)
EnterMove(board=playboard)
DisplayBoard(board=playboard)
MakeListOfFreeFields(board=playboard)
DrawMove(board=playboard)
EnterMove(board=playboard)
DisplayBoard(board=playboard)
MakeListOfFreeFields(board=playboard)
DrawMove(board=playboard)
VictoryFor(board=playboard,sign="X")
EnterMove(board=playboard)
DisplayBoard(board=playboard)
VictoryFor(board=playboard,sign="X")
MakeListOfFreeFields(board=playboard)
DrawMove(board=playboard)
VictoryFor(board=playboard,sign="X")






