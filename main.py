import random
import time

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
welcome_b = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
how_to_b = [['(1 1)', '(1 2)', '(1 3)'], ['(2 1)', '(2 2)', '(2 3)'], ['(3 1)', '(3 2)', '(3 3)']]


def main_menu():
    print('  ', 'Welcome to the game.', '\n\t\t', *welcome_b[0], '\n\t\t', *welcome_b[1], '\n\t\t', *welcome_b[2])
    time.sleep(1)
    print('\nPlease choose your action from the menu:', "\n'1'- Start game.\n'2'- How to play.\n'3'- Exit.")
    while True:
        menu_choose = input('Provide an input: ')
        if not menu_choose.isdigit():
            print('You should enter a number.')
            continue
        if len(menu_choose) != 1:
            print('You should enter a number of your choice.')
            continue
        if not (1 <= int(menu_choose) <= 3):
            print('Selection should be from 1 to 3')
            continue
        if int(menu_choose) == 1:
            start_game()
            break
        elif int(menu_choose) == 2:
            how_to_play()
            break
        elif int(menu_choose) == 3:
            exit()
        else:
            print('Wrong entry. Please re-enter your choice.')
            continue


def end_game_menu():
    print('\nGame over.\nChoose your action:')
    print("\n'1'- Quick restart.\n'2'- Go to main menu.\n'Any key'- Exit.\n")
    end_game_input = input('Provide an input: ')
    if end_game_input == '1':
        start_game()
    elif end_game_input == '2':
        main_menu()
    else:
        exit()


def start_game():
    for i in range(2):
        user_move()
        time.sleep(1)
        computer_move()
        time.sleep(1)
    for i in range(5):
        user_move()
        check_game()
        computer_move()
        check_game()


# Eklemeler yapılacak. Yazdirma islemleri duzenlenecek.
def how_to_play():
    print('\nHow to Play:')
    print('How should I write my moves. / Possible move coordinates on the board.')
    print('-----------------------')
    print('| ', *how_to_b[0], ' |', '\n| ', *how_to_b[1], ' |', '\n| ', *how_to_b[2], ' |')
    print('-----------------------')
    print('Valid move example: 2 1')


def print_board():
    print("---------")
    for i in range(len(board)):
        print("|", end=" ")
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print('|')
    print('---------')


# Kosullari duzenle/kisalt.
def check_game():
    if all('X' in a for a in board[0]) or all('X' in a for a in board[1]) or all('X' in a for a in board[2]):
        x_wins()
    elif ('X' == board[0][0]) and ('X' == board[1][0]) and ('X' == board[2][0]):
        x_wins()
    elif ('X' == board[0][1]) and ('X' == board[1][1]) and ('X' == board[2][1]):
        x_wins()
    elif ('X' == board[0][2]) and ('X' == board[1][2]) and ('X' == board[2][2]):
        x_wins()
    elif ('X' == board[0][0]) and ('X' == board[1][1]) and ('X' == board[2][2]):
        x_wins()
    elif ('X' == board[0][2]) and ('X' == board[1][1]) and ('X' == board[2][0]):
        x_wins()
    elif all('O' in a for a in board[0]) or all('O' in a for a in board[1]) or all('O' in a for a in board[2]):
        o_wins()
    elif ('O' == board[0][0]) and ('O' == board[1][0]) and ('O' == board[2][0]):
        o_wins()
    elif ('O' == board[0][1]) and ('O' == board[1][1]) and ('O' == board[2][1]):
        o_wins()
    elif ('O' == board[0][2]) and ('O' == board[1][2]) and ('O' == board[2][2]):
        o_wins()
    elif ('O' == board[0][0]) and ('O' == board[1][1]) and ('O' == board[2][2]):
        o_wins()
    elif ('O' == board[0][2]) and ('O' == board[1][1]) and ('O' == board[2][0]):
        o_wins()
    elif not any(' ' in sl for sl in board):
        print("Draw")
        end_game_menu()
    else:
        time.sleep(1)
        return


def x_wins():
    print('X Wins.')
    time.sleep(1)
    end_game_menu()


def o_wins():
    print('O Wins.')
    time.sleep(1)
    end_game_menu()


def check_for_ai():
    if any(' ' in sl for sl in board):
        return True


def computer_move():
    if check_for_ai():
        comp_coord = random.randrange(0, 3), random.randrange(0, 3)
        if board[comp_coord[0]][comp_coord[1]] != ' ':
            return computer_move()
        else:
            board[comp_coord[0]][comp_coord[1]] = 'O'
        comp_coord = [int(ui) + 1 for ui in comp_coord]
        print('\nComputers Move: ', comp_coord)
    print_board()


def get_coordinates():
    while True:
        print('Enter Coordinates:', end=' ')
        coord_input = input().split()
        if not coord_input[0].isdigit() or not coord_input[1].isdigit():
            print('You should enter numbers!')
            continue
        if len(coord_input) != 2:
            print('You should enter two numbers of coordinates.')
            continue

        coord_input = [int(ui) - 1 for ui in coord_input]

        if not (0 <= coord_input[0] < 3 and 0 <= coord_input[1] < 3):
            print('Coordinates should be from 1 to 3!')
            continue
        if board[coord_input[0]][coord_input[1]] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        break
    return coord_input


def user_move():
    print('\nUser\'s Move: ')
    user_coord = get_coordinates()
    board[user_coord[0]][user_coord[1]] = 'X'
    print_board()


if __name__ == '__main__':
    main_menu()
