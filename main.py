import random

board = [['\t', '\t', '\t'], ['\t', '\t', '\t'], ['\t', '\t', '\t']]


def print_board():
    print("--------------")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print('|')
    print('--------------')


# Oyun kazanma şartları ve oyun bitme şartları ekle.
def check_game():
    for i in board:
        if i[0] == 'X\t' and i[1] == 'X\t' and i[2] == 'X\t':
            print("X Wins")
            exit()
        elif i[0] == 'O\t' and i[1] == 'O\t' and i[2] == 'O\t':
            print("O Wins")
            exit()


# Board dolu olduğunda check_game()den exite döndür.
def computer_move():
    check_game()
    comp_coor = random.randrange(0, 3), random.randrange(0, 3)
    if board[comp_coor[0]][comp_coor[1]] == 'X\t' or board[comp_coor[0]][comp_coor[1]] == 'O\t':
        return computer_move()
    else:
        board[comp_coor[0]][comp_coor[1]] = 'O\t'
    print("Computers Move:")
    print_board()


def get_coordinates():
    print("Enter Coordinates: ")
    coor_input = list(map(int, input().split()))
    coor_input = [abs(x) for x in coor_input]
    if coor_input[0] > 2 or coor_input[1] > 2:
        print("Please provide coordinates between 0..2")
    else:
        return coor_input


def user_move():
    check_game()
    user_coor = get_coordinates()
    if board[int(user_coor[0])][int(user_coor[1])] == 'X\t' or board[int(user_coor[0])][int(user_coor[1])] == 'O\t':
        print("This slot is full, try empty one.")
        return user_move()
    else:
        board[int(user_coor[0])][int(user_coor[1])] = 'X\t'
    print("Users Move:")
    print_board()


if __name__ == '__main__':
    for i in range(9):
        user_move()
        computer_move()
