"""
ICS32 Project 2
Navigator: Wenyu Ouyang ID:23402729
Driver:Yizhuo Wu ID:14863527
"""

import connectfour
def welcome_user()->None:
    '''
    This function will welcome the user when the user run the program.
    '''
    print("Welcome to the world of connectfour.")
    print()
def print_column_board(board:[[int]],row:int)->str:
    '''
    Print each column using '.', the program will replace the '0' by '.','1'
    by 'R','2' by 'Y'. 
    '''
    for col in board:
        if col[row]==0:
            print('.',end=' ')
        elif col[row]==1:
            print('R', end=' ')
        elif col[row]==2:
            print('Y',end=' ')

def print_game_board(board:[[int]])->str:
    '''
    This function will print the whole game board to the user.
    '''
    for order in range(1,connectfour.BOARD_COLUMNS+1):
        print(order, end=' ')
        
    print('\r')
    for row in range(connectfour.BOARD_ROWS):
        print_column_board(board,row)
        print('\r')

def get_user_cmd()->str:
    '''
    This function will get the command from the user.
    If the command entered by user is neither 'Drop' nor
    'Pop', the function will prompt the user to enter it again
    until the command is valid.
    '''
    cmdlist=['POP','DROP']
    
    while True:
        cmd=input("Do you want to drop or pop? ")
        if cmd.upper() in cmdlist:
            return cmd
        print("Invalid action.")

def get_col_number()->int:
    '''
    This function will get the column number from the user.
    If the column number entered by user is not an integer or
    it's empty, the function will prompt the user to enter it again
    until the column number is valid.
    '''
    while True:
        try:
            col_number=int(input("Enter the column number you want to drop or pop? "))-1
            return col_number
            
        except ValueError:
            print("Invalid column number")

