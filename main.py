import random
import time

board = [['\t', '\t', '\t'], ['\t', '\t', '\t'], ['\t', '\t', '\t']]
welcome_b = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
howto_b = [['(0 0)', '(0 1)', '(0 2)'], ['(1 0)', '(1 1)', '(1 2)'], ['(2 0)', '(2 1)', '(2 2)']]


def game_menu():
    print('  ', 'Welcome to the game.', '\n\t\t', *welcome_b[0], '\n\t\t', *welcome_b[1], '\n\t\t', *welcome_b[2])
    time.sleep(1)
    print('\nPlease choose your action from the menu:', "\n'1'- Start game.\n'2'- Command list.\n'3'- Exit.")
    menu_choose = input('Provide an input: ')
    if menu_choose == '1' or menu_choose == 'start':
        start_game()
    elif menu_choose == '2' or menu_choose == 'commands':
        howto_play()
    elif menu_choose == '3' or menu_choose == 'exit':
        exit()
    else:
        # Menu secimine don.
        print('Wrong entry.')


def start_game():
    for i in range(9):
        user_move()
        time.sleep(1)
        computer_move()
        time.sleep(1)


# Eklemeler yapılacak. Yazdirma islemleri duzenlenecek.
def howto_play():
    print('\nHow to Play:')
    print('How should I write my moves. / Possible move coordinates on the board.')
    print('-----------------------')
    print('| ', *howto_b[0], ' |', '\n| ', *howto_b[1], ' |', '\n| ', *howto_b[2], ' |')
    print('-----------------------')
    print('Valid move example: 2 1')


def print_board():
    print("--------------")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print('|')
    print('--------------')


# Tum kosullari ekle, Restart ekle.
def check_winner():
    for i in board:
        if i[0] == 'X\t' and i[1] == 'X\t' and i[2] == 'X\t':
            print('X Wins')
            exit()
        elif i[0] == 'O\t' and i[1] == 'O\t' and i[2] == 'O\t':
            print('O Wins')
            exit()


# Restart ekle
def check_game():
    if any('\t' in sl for sl in board):
        return
    else:
        check_winner()
        print('Board is full, game over.')
        exit()


def computer_move():
    check_game()
    comp_coor = random.randrange(0, 3), random.randrange(0, 3)
    if board[comp_coor[0]][comp_coor[1]] == 'X\t' or board[comp_coor[0]][comp_coor[1]] == 'O\t':
        return computer_move()
    else:
        board[comp_coor[0]][comp_coor[1]] = 'O\t'
    print('\nComputers Move: ', comp_coor)
    print_board()


def get_coordinates():
    print('Enter Coordinates:', end=' ')
    coor_input = list(map(int, input().split()))
    coor_input = [abs(x) for x in coor_input]
    if coor_input[0] > 2 or coor_input[1] > 2:
        print('Please provide coordinates between 0..2')
    else:
        return coor_input


def user_move():
    print('\nUsers Move: ')
    user_coor = get_coordinates()
    if board[int(user_coor[0])][int(user_coor[1])] == 'X\t' or board[int(user_coor[0])][int(user_coor[1])] == 'O\t':
        print('This slot is full, try empty one.')
        return user_move()
    else:
        board[int(user_coor[0])][int(user_coor[1])] = 'X\t'
    print_board()


if __name__ == '__main__':
    game_menu()
