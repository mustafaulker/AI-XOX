from random import randrange
import time

main_board = [['', '', ''], ['', '', ''], ['', '', '']]
intro_b = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
how_to_b = [['(1 1)', '(1 2)', '(1 3)'], ['(2 1)', '(2 2)', '(2 3)'], ['(3 1)', '(3 2)', '(3 3)']]


# Intro Message
def intro():
    print('  ', 'Welcome to the game.', '\n\t\t', *intro_b[0], '\n\t\t', *intro_b[1], '\n\t\t', *intro_b[2])
    time.sleep(1)


# Creation of empty board
def generate_board():
    for i in range(3):
        for j in range(3):
            main_board[i][j] = ' '


# Main Menu
def main_menu():
    print('\nPlease choose your action from the menu:', "\n'1'- Start game.\n'2'- How to play.\n'3'- Exit.")
    while True:
        menu_choose = input('Provide an input: ')
        # Input checks
        if not menu_choose.isdigit():
            print('You should enter a number.')
            continue
        if len(menu_choose) != 1:
            print('You should enter a number of your choice.')
            continue
        if not (1 <= int(menu_choose) <= 3):
            print('Selection should be from 1 to 3')
            continue
        # Menu options
        if int(menu_choose) == 1:
            generate_board()
            level_chooser()
            break
        elif int(menu_choose) == 2:
            how_to_play()
            break
        elif int(menu_choose) == 3:
            exit()
        else:
            print('Wrong entry. Please re-enter your choice.')
            continue


# Level selection
def level_chooser():
    while True:
        print("\nChoose AI Level: \n'1'- Easy \n'2'- Medium \n'3'- Hard")
        level_choose = input('Your choice: ')
        # Input checks
        if len(level_choose) != 1:
            print('You should enter a number of your choice.')
            continue
        if not (1 <= int(level_choose) <= 3):
            print('Selection should be from 1 to 3')
            continue
        # Level options
        if int(level_choose) == 1:
            game_operation('1')
        elif int(level_choose) == 2:
            game_operation('2')
        elif int(level_choose) == 3:
            game_operation('3')
        else:
            print('Wrong entry. Please re-enter your choice.')
            continue


# End game menu
def end_game_menu():
    print('\nGame over.\nChoose your action:'
          "\n'1'- Quick restart.\n'2'- Go to main menu.\n'Any key'- Exit.\n")
    end_game_input = input('Provide an input: ')
    if end_game_input == '1':
        generate_board()
        level_chooser()
    elif end_game_input == '2':
        print('\n')
        main_menu()
    else:
        exit()


# Game logic based on level selection
def game_operation(levelchoose):
    if levelchoose == '1':
        while 1:
            user_move()
            easy_ai_move()
    elif levelchoose == '2':
        while 1:
            user_move()
            medium_ai_move()
    elif levelchoose == '3':
        while 1:
            user_move()
            hard_ai_move()


# How to play message
def how_to_play():
    print('\nHow to Play:\nPossible move coordinates on the board.\n-----------------------'
          '\n| ', *how_to_b[0], ' |', '\n| ', *how_to_b[1], ' |', '\n| ', *how_to_b[2], ' |'
          '\n-----------------------\nValid move example: "2 1"')
    if input('\nProvide any input to return: '):
        main_menu()


# Printing the board
def board_printer():
    print("---------")
    for i in range(len(main_board)):
        print("|", end=" ")
        for j in range(len(main_board[i])):
            print(main_board[i][j], end=" ")
        print('|')
    print('---------')


# Winner control
def winner_determination():
    # Horizontal check
    for i in range(0, 3):
        if main_board[i] == ['X', 'X', 'X']:
            return 'X'
        elif main_board[i] == ['O', 'O', 'O']:
            return 'O'
    # Vertical check
    for i in range(0, 3):
        if (main_board[0][i] != ' ' and
                main_board[0][i] == main_board[1][i] and
                main_board[1][i] == main_board[2][i]):
            return main_board[0][i]
    # Diagonal check 1
    if (main_board[0][0] != ' ' and
            main_board[0][0] == main_board[1][1] and
            main_board[0][0] == main_board[2][2]):
        return main_board[0][0]
    # Diagonal check 2
    if (main_board[0][2] != ' ' and
            main_board[0][2] == main_board[1][1] and
            main_board[0][2] == main_board[2][0]):
        return main_board[0][2]
    return ' '


# Game state check
def any_winner():
    if winner_determination() == 'X':
        winner_is('X')
    elif winner_determination() == 'O':
        winner_is('O')
    elif not any(' ' in sl for sl in main_board):
        print("Draw")
        time.sleep(2)
        end_game_menu()
    else:
        time.sleep(1)
        return


# If there is a winner
def winner_is(winner):
    if winner == 'X':
        print('X Wins.')
        time.sleep(2)
        end_game_menu()
    else:
        print('O Wins.')
        time.sleep(2)
        end_game_menu()


# Easy level AI move
def easy_ai_move():
    if any(' ' in sl for sl in main_board):  # Empty slot check
        while 1:
            comp_coord = randrange(0, 3), randrange(0, 3)  # Generating random coordinates
            if main_board[comp_coord[0]][comp_coord[1]] != ' ':  # Check if generated coordinates are empty
                continue
            else:
                # If empty, do the move. Print the coordinates by increasing the values by 1
                main_board[comp_coord[0]][comp_coord[1]] = 'O'
                print('\nAI Move: ', comp_coord[0] + 1, comp_coord[1] + 1)
                break
    board_printer()
    any_winner()


# Medium level AI move.
def medium_ai_move():
    for i in range(len(main_board)):
        for j in range(len(main_board[i])):
            if main_board[i][j] == ' ':
                main_board[i][j] = 'O'
                # If AI can win in the next round
                if winner_determination() == 'O':
                    print(f'\nAI Move: {i + 1} {j + 1}')
                    board_printer()
                    any_winner()
                    return True
                else:
                    main_board[i][j] = 'X'
                    # If the user can win in the next round
                    if winner_determination() == 'X':
                        main_board[i][j] = 'O'
                        print(f'\nAI Move: {i + 1} {j + 1}')
                        board_printer()
                        any_winner()
                        return True
                    else:
                        main_board[i][j] = ' '
            else:
                continue
    easy_ai_move()


# Determination of which player is playing on the next round. (hard_ai_move() component)
x_turn = False


# Conversion of the moves. (hard_ai_move() component)
def convert_move_coord(x, y):
    return 3 - y, x - 1


# Check if the next coordinates are occupied. (hard_ai_move() component)
def check_cell_is_occupied(x, y):
    i, j = convert_move_coord(x, y)
    if main_board[i][j] != ' ':
        return True
    return False


# Make move to determined coordinates. (hard_ai_move() component)
def make_move(x, y):
    global x_turn
    i, j = convert_move_coord(x, y)
    main_board[i][j] = "X" if x_turn else "O"
    x_turn = not x_turn


# Undo the last move. (hard_ai_move() component)
def undo_move(x, y):
    global x_turn
    i, j = convert_move_coord(x, y)
    main_board[i][j] = ' '
    x_turn = not x_turn


# Hard Level AI move. (Minimax Algorithm)
def hard_ai_move():
    global x_turn
    max_score = -100
    best_move = [0, 0]
    start = time.time()
    for i in range(1, 4):
        for j in range(1, 4):
            if not check_cell_is_occupied(i, j):
                x_turn = False
                make_move(i, j)
                current_score = minimax_score_calc(False)
                if current_score > max_score:
                    max_score = current_score
                    best_move = [i, j]
                undo_move(i, j)
    make_move(best_move[0], best_move[1])
    print("\nCalculation time: ", round(time.time() - start, 3), "seconds.")
    hard_x_coord, hard_y_coord = convert_move_coord(best_move[0], best_move[1])
    print("AI Move: ", hard_x_coord + 1, hard_y_coord + 1)
    board_printer()
    any_winner()


# Score calculation for Minimax. (hard_ai_move() component)
def minimax_score_calc(is_max):
    winner = winner_determination()
    if winner == 'O':
        return 10
    elif winner != ' ':
        return -10
    else:
        if not any(' ' in sl for sl in main_board):
            return 0
        else:
            if is_max:
                target_score = -100
                for i in range(1, 4):
                    for j in range(1, 4):
                        if not check_cell_is_occupied(i, j):
                            make_move(i, j)
                            target_score = max(minimax_score_calc(False), target_score)
                            undo_move(i, j)
            else:
                target_score = 100
                for i in range(1, 4):
                    for j in range(1, 4):
                        if not check_cell_is_occupied(i, j):
                            make_move(i, j)
                            target_score = min(minimax_score_calc(True), target_score)
                            undo_move(i, j)
    return target_score


# Get coordinates from the user, check the input (user_move() component)
def get_coordinates():
    while True:
        print('Enter Coordinates:', end=' ')
        coord_input = input().split()
        if not coord_input[0].isdigit() or not coord_input[1].isdigit():  # Input checks
            print('You should enter numbers!')
            continue
        if len(coord_input) != 2:
            print('You should enter two numbers of coordinates.')
            continue

        coord_input = [int(ui) - 1 for ui in coord_input]  # Decreasing of input coordinates. '1 2' -> '0 1'

        if not (0 <= coord_input[0] < 3 and 0 <= coord_input[1] < 3):
            print('Coordinates should be from 1 to 3!')
            continue
        if main_board[coord_input[0]][coord_input[1]] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        break
    return coord_input


# User move
def user_move():
    print('\nUser\'s Move: ')
    user_coord = get_coordinates()
    main_board[user_coord[0]][user_coord[1]] = 'X'
    board_printer()
    any_winner()


if __name__ == '__main__':
    intro()
    main_menu()
