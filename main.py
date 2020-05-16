from random import randrange
from time import sleep

main_board = [['', '', ''], ['', '', ''], ['', '', '']]
intro_b = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
how_to_b = [['(1 1)', '(1 2)', '(1 3)'], ['(2 1)', '(2 2)', '(2 3)'], ['(3 1)', '(3 2)', '(3 3)']]


# Oyun baslangic mesaji
def intro():
    print('  ', 'Welcome to the game.', '\n\t\t', *intro_b[0], '\n\t\t', *intro_b[1], '\n\t\t', *intro_b[2])
    sleep(1)


# Bos board yaratma
def generate_board():
    for i in range(3):
        for j in range(3):
            main_board[i][j] = ' '


# Ana menu
def main_menu():
    print('\nPlease choose your action from the menu:', "\n'1'- Start game.\n'2'- How to play.\n'3'- Exit.")
    while True:
        menu_choose = input('Provide an input: ')
        # Girdi kontrolleri
        if not menu_choose.isdigit():
            print('You should enter a number.')
            continue
        if len(menu_choose) != 1:
            print('You should enter a number of your choice.')
            continue
        if not (1 <= int(menu_choose) <= 3):
            print('Selection should be from 1 to 3')
            continue
        # Menu secenekleri
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


# Level secimi
def level_chooser():
    while True:
        print("\nChoose AI Level: \n'1'- Easy \n'2'- Medium \n'3'- Hard(Will be added)")
        level_choose = input('Your choice: ')
        # Girdi kontrolleri
        if len(level_choose) != 1:
            print('You should enter a number of your choice.')
            continue
        if not (1 <= int(level_choose) <= 3):
            print('Selection should be from 1 to 3')
            continue
        # Level secenekleri
        if int(level_choose) == 1:
            game_operation('1')
        elif int(level_choose) == 2:
            game_operation('2')
        elif int(level_choose) == 3:
            print('\nHard level will be added soon.')
            continue
        else:
            print('Wrong entry. Please re-enter your choice.')
            continue


# Oyun sonu menusu
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


# Level secimine bagli oyun isleyisi
def game_operation(levelchoose):
    if levelchoose == '1':
        while 1:
            user_move()
            easy_ai_move()
    elif levelchoose == '2':
        while 1:
            user_move()
            medium_ai_move()


# How to play mesaji
def how_to_play():
    print('\nHow to Play:'
          '\nPossible move coordinates on the board.'
          '\n-----------------------'
          '\n| ', *how_to_b[0], ' |', '\n| ', *how_to_b[1], ' |', '\n| ', *how_to_b[2], ' |'
          '\n-----------------------'
          '\nValid move example: "2 1"')
    if input('\nProvide any input to return: '):
        main_menu()


# Board yazdirma
def board_printer():
    print("---------")
    for i in range(len(main_board)):
        print("|", end=" ")
        for j in range(len(main_board[i])):
            print(main_board[i][j], end=" ")
        print('|')
    print('---------')


# Oyunun devam edip etmedigini / Kazanani kontrol etme
# Medium level AI hamlesi icin olası senaryo testlerinde kullanilacak hamle sonucu testi
def check_board():
    # Yatay kontrol
    for i in range(0, 3):
        if main_board[i] == ['X', 'X', 'X']:
            return 'X'
        elif main_board[i] == ['O', 'O', 'O']:
            return 'O'
    # Dikey kontrol
    for i in range(0, 3):
        if (main_board[0][i] != ' ' and
                main_board[0][i] == main_board[1][i] and
                main_board[1][i] == main_board[2][i]):
            return main_board[0][i]
    # Capraz kontrol 1
    if (main_board[0][0] != ' ' and
            main_board[0][0] == main_board[1][1] and
            main_board[0][0] == main_board[2][2]):
        return main_board[0][0]
    # Capraz kontrol 2
    if (main_board[0][2] != ' ' and
            main_board[0][2] == main_board[1][1] and
            main_board[0][2] == main_board[2][0]):
        return main_board[0][2]


def check_game():
    if check_board() == 'X':
        winner_is('X')
    elif check_board() == 'O':
        winner_is('O')
    elif not any(' ' in sl for sl in main_board):
        print("Draw")
        sleep(2)
        end_game_menu()
    else:
        sleep(1)
        return


# Kazanan oldugunda yapilacak islem
def winner_is(winner):
    if winner == 'X':
        print('X Wins.')
        sleep(2)
        end_game_menu()
    else:
        print('O Wins.')
        sleep(2)
        end_game_menu()


# Easy level AI hamlesi
def easy_ai_move():
    if any(' ' in sl for sl in main_board):  # Bos yuva kontrolu
        while 1:
            comp_coord = randrange(0, 3), randrange(0, 3)  # Random koordinat elde etme
            if main_board[comp_coord[0]][comp_coord[1]] != ' ':  # Eger random koordinat yuvası bos degilse tekrar uret
                continue
            else:
                main_board[comp_coord[0]][comp_coord[1]] = 'O'  # Bos ise hamleyi yap, degerleri 1 arttirarak yazdir
                print('\nAI Move: ', comp_coord[0]+1, comp_coord[1]+1)
                break
    board_printer()
    check_game()


# AI ve Kullanicinin gelecek hamlede kazanip kazanamayacagi kontrolu.
# AI'in kazanabildigi senaryoda hamlesini kazanan koordinata yapacak.
# Kullanicinin kazanabildigi senaryoda, hamlesini blocklayan koordinata yapacak.
def can_ai_win_block():
    duplicate_board = main_board
    for i in range(len(duplicate_board)):
        for j in range(len(duplicate_board[i])):
            if duplicate_board[i][j] == ' ':
                duplicate_board[i][j] = 'O'
                if check_board() == 'O':
                    main_board[i][j] = 'O'
                    print(f'\nAI Move: [{i+1}, {j+1}]')
                    board_printer()
                    check_game()
                    return True
                else:
                    duplicate_board[i][j] = 'X'
                    if check_board() == 'X':
                        main_board[i][j] = 'O'
                        print(f'\nAI Move: [{i + 1}, {j + 1}]')
                        board_printer()
                        check_game()
                        return True
                    else:
                        duplicate_board[i][j] = ' '
            else:
                continue


# Medium level AI hamlesi.
# Kazanma ya da block senaryosu olmadigi durumlarda random hamle yapacak.
def medium_ai_move():
    if can_ai_win_block():
        return
    else:
        easy_ai_move()


# Kullanicidan koordinat istemi ve girdi kontrolu
def get_coordinates():
    while True:
        print('Enter Coordinates:', end=' ')
        coord_input = input().split()
        if not coord_input[0].isdigit() or not coord_input[1].isdigit():  # Girdi kontrolleri
            print('You should enter numbers!')
            continue
        if len(coord_input) != 2:
            print('You should enter two numbers of coordinates.')
            continue

        coord_input = [int(ui) - 1 for ui in coord_input]  # Girdi degerlerinin 1 dusurulmesi. '1 2' -> '0 1'

        if not (0 <= coord_input[0] < 3 and 0 <= coord_input[1] < 3):
            print('Coordinates should be from 1 to 3!')
            continue
        if main_board[coord_input[0]][coord_input[1]] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        break
    return coord_input


# Kullanici hamlesi
def user_move():
    print('\nUser\'s Move: ')
    user_coord = get_coordinates()
    main_board[user_coord[0]][user_coord[1]] = 'X'
    board_printer()
    check_game()


if __name__ == '__main__':
    intro()
    main_menu()
