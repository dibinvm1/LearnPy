import os
import random
def display_board(board):
    os.system('CLS')
    print("!!!TIC TAC TOE!!!")
    print('  '+board[1]+' | ' + board [2]+ ' | ' + board[3])
    print('------------')
    print('  '+board[4]+' | ' + board [5]+ ' | ' + board[6])
    print('------------')
    print('  '+board[7]+' | ' + board [8]+ ' | ' + board[9])
def player_input():
    '''
    #OUTPUT = (player1,player2)
    '''
    #Taking input from players to choose their markers
    marker = ''
    while marker != 'O' and marker != 'X':
        marker = input('Player 1 Choose one marker X or O :').upper()
        if marker == 'X':
            return('X','O')
        else:
            return('O','X')
def marker_position(board,marker,position):
    '''
    INPUT = board[],O or X,position 1-9
    '''
    #placing marker in the desired Position
    board[position] = marker
def check_win(board,marker):
    '''
    INPUT  = board[],X or O
    OUTPUT = True or False
    '''
    #checking if the player has won
    return ((board[1] == board [2] == board[3] == marker) or # first row
            (board[4] == board [5] == board[6] == marker) or #second row
            (board[7] == board [8] == board[9] == marker) or #third row
            (board[1] == board [4] == board[7] == marker) or #first Column
            (board[2] == board [5] == board[8] == marker) or #second Column
            (board[3] == board [6] == board[9] == marker) or #third Column
            (board[1] == board [5] == board[9] == marker) or #diagonal
            (board[3] == board [5] == board[7] == marker)) #diagonal
def who_goes_first():
    #randomly dicides who goes first using randint()
    check = random.randint(0,1)
    res = 'Player 1' if check == 0 else 'Player 2'
    return res
def check_space(board,position):
    #checking is a position in board is free
    return (board[position] == ' ')
def check_board_full(board):
    i =1
    while(i<10):
        if check_space(board,i): #checking space avliable or not for all spaces
            return False
        i+=1
    return True
def ask_player_pos(board):
    choice = 0
    while choice not in range(1,10) or not check_space(board,choice):
        choice = int(input('Enter a position [1-9] :'))
    return choice
def play_again():
    res = input('Want to Play again ? Yes(Y) or No(N) :').upper()
    return res == 'Y'
def play_game():
    #driver function
    game_on = True
    while game_on:
        board = [' ']*10 # str
        player1,player2 = player_input()
        turn = who_goes_first()
        print(turn + " GOES FIRST!!")
        play_game = input('Are you ready to play? Enter Yes or No.')
        if play_game.lower()[0] == 'y':
            playing = True
        else:
            playing = False
        while(playing):
            if turn == 'Player 1':
                display_board(board)
                print("Palyer 1 's Turn ")
                position = ask_player_pos(board)
                marker_position(board,player1,position)
                if check_win(board,player1):
                    display_board(board)
                    print("Player 1 Won The game")
                    playing = False
                elif check_board_full(board):
                    display_board(board)
                    print("IT'S A TIE")
                    playing = False
                else:
                    turn = 'Player 2'
            else:
                display_board(board)
                print("Palyer 2 's Turn ")
                position = ask_player_pos(board)
                marker_position(board,player2,position)
                if check_win(board,player2):
                    display_board(board)
                    print("Player 2 Won The game")
                    playing = False
                elif check_board_full(board):
                    display_board(board)
                    print("IT'S A TIE")
                    playing = False
                else:
                    turn = 'Player 1'
        if not play_again():
            game_on = False

if __name__ == "__main__":
        play_game()