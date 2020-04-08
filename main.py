import random

board = [['\t', '\t', '\t'], ['\t', '\t', '\t'], ['\t', '\t', '\t']]


def getCoordinates():
    print("Enter Coordinates : ")
    currentCoor = str.split(input())
    board[int(currentCoor[0])][int(currentCoor[1])] = 'X\t'


def computerMove():
    comp_coor1 = random.randrange(0, 3)
    comp_coor2 = random.randrange(0, 3)
    board[comp_coor1][comp_coor2] = '0\t'
    print("--------------")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print('|')
    print('--------------')


def makeMove():
    getCoordinates()
    print("--------------")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print('|')
    print('--------------')




