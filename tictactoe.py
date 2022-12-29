x_player = False
o_player = False
game_board = ['#','1','2','3','4','5','6','7','8','9']
exit = False


def display(board):
    board_length = len(board)
    board_top = '   |   |    '
    board_middle = '___|___|___'
    #board_top = [' ', ' ', ' ', '|',' ', ' ', ' ', '|',' ', ' ', ' ', '|' ]
    print(board_top)
    print(f' {board[board_length - 3]} | {board[board_length - 2]} | {board[board_length- 1]} ')
    print(board_middle)
    print(board_top)
    print(f' {board[board_length - 6]} | {board[board_length - 5]} | {board[board_length- 4]} ')
    print(board_middle)
    print(board_top)
    print(f' {board[board_length - 9]} | {board[board_length - 8]} | {board[board_length- 7]} ')
    print(board_top)



def player_input(player1, player2):
    player_choice = 'WRONG'
    while player_choice not in ['X', 'O', 'Q']:        
        player_choice = input('\nWho would you like to go first X or O? ')
        player_choice = player_choice.upper()
        if player_choice not in ['X', 'O']:
            print('\nInvalid choice select either X or O\n')
        elif player_choice == 'X':
            player1 = True
            player2 = False
            print('You have chosen for X to go first\n')
            return player1, player2 
        elif player_choice == 'O':
            player1 = False
            player2 = True
            print('You have chosen for 0 to go first\n')
            return player1, player2

def select_square():
    global x_player
    global o_player
    global game_board
    global exit
    choice = 'WRONG'
    refresh_flag = False
    while choice not in range(0,10) or exit == False or refresh_flag == False:
            if x_player == True:
                choice = input('Player X select what square you would like to place (1-9)\nYou may also enter Q to quit or R to refresh the board: ')
                #choice = int(choice)
                if choice not in game_board and choice not in ['Q', 'q',]:
                    print('\nYour selection is invalid')
                elif choice in ['Q', 'q'] :
                    exit = True
                    break
                else:
                    return int(choice)
            if o_player == True: 
                choice = input('Player O select what square you would like to place (1-9)\nYou may also enter Q to quit or R to refresh the board: ')
                #choice = int(choice)
                if choice in ['Q', 'q']:
                    exit = True
                    break
                elif choice in ['R', 'r']:
                    refresh_board()
                    refresh_flag = True
                    break
                elif choice not in game_board:
                    print('\nYour selection is invalid')
                else:
                    return int(choice)
                
def place_square(location):
    global game_board
    global x_player
    global o_player
    player = 'WRONG'
    #print(player)
    while player not in ['X', 'O']:
        if x_player == True:
            player = 'X'
            if str(location) in game_board:
                game_board[location] = player
                x_player = False
                o_player = True
        elif o_player == True:
            player = 'O'
            if str(location) in game_board:
                game_board[location] = player
                x_player = True
                o_player = False
        else:
            pass

def refresh_board(): 
    global x_player
    global o_player
    global game_board
    x_player = False
    o_player = False
    game_board = ['#','1','2','3','4','5','6','7','8','9']
    print('\nBoard has been refreshed!')
    x_player,o_player = player_input(x_player, o_player)

def winner_detection(current_board):
    x_win = ['X', 'X', 'X']
    o_win = ['O', 'O', 'O']
    diag1 = [1, 5, 9]
    diag2 = [7, 5, 3]
    x_diag1 = [current_board[i] for i in diag1]
    x_diag2 = [current_board[i] for i in diag2]
    for i in range(len(current_board) - len(x_win) + 1):
        if i == 2 or i == 3 or i == 6:
            continue
        elif current_board[i:i+len(x_win)] == x_win:
                print('\nX has won!')
                refresh_board()
                break
        elif x_diag1 == x_win or x_diag2 == x_win:
                print('\nX has won!')
                refresh_board()
                break
    for i in range(len(current_board) - len(o_win) + 1):
        if i == 2 or i == 3 or i == 6:
            continue
        elif current_board[i:i+len(o_win)] == o_win:
                print('\nO has won!')
                refresh_board()
                break
        elif x_diag1 == o_win or x_diag2 == o_win:
                print('\nO has won!')
                refresh_board()
                break   


    

def main():
    global x_player
    global o_player
    global game_board
    global exit
    print('Welcome to tic tac toe!\nFirst let select what player you would like to go first\n')
    x_player,o_player = player_input(x_player, o_player)
    while not exit:
        display(game_board)
        player_choice = select_square()
        # print(player_choice)
        place_square(player_choice)
        winner_detection(game_board)
main()
