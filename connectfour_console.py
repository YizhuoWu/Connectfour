"""
ICS32 Project 2
Navigator: Wenyu Ouyang ID:23402729
Driver:Yizhuo Wu ID:14863527
"""

import connectfour
import common_functions
 
    
def run_step(game_state)->None:
    '''
    This function will run the game steps. First, it checks whether the game is over(If there is
    a winner). If not, then it checks who's turn at that moment should be. If it's red turn, it
    will get the command and column number from the red user. If it's yellow's turn, it will get them from
    the yellow player. Then it will proceed the command, if the command is 'drop', it will run the drop
    function and print the board to the user. If the command is 'pop', it will run the pop
    function and print the board to the user. When one of the player won, it print the congratulations
    message and end the game.
    '''
    if connectfour.winner(game_state)==connectfour.NONE:
        if game_state.turn==1:
            print("This is the red 's turn")
        elif game_state.turn==2:
            print("This is the yellow 's turn")
        cmd=common_functions.get_user_cmd()
        column_number=common_functions.get_col_number()
        
        try:
            if cmd.upper()=='DROP':
                new_game_state=connectfour.drop(game_state,column_number)
                common_functions.print_game_board(new_game_state.board)
                run_step(new_game_state)
           

            elif cmd.upper()=="POP":
                new_game_state=connectfour.pop(game_state,column_number  )
                common_functions.print_game_board(new_game_state.board)
                run_step(new_game_state)
                
        except connectfour.InvalidMoveError:
            print()
            print("Invalid Move! Please try again!")
            print()
            run_step(game_state)

    elif connectfour.winner(game_state)==1 :
        print()
        print("Game is over!")
        print("Congratulations! The Red player is the winner!") 
    
    elif connectfour.winner(game_state)==2 :
        print()
        print("Game is over!")
        print("Congratulations! The Yellow player is the winner!") 

def main():
    '''
    This function will first get a new game state(Create an empty game board
    and set the first turn to red. Then it will welcome the user and print an
    empty board. Then it run the whole game until a winner occurs and it ends
    the program.)
    '''
    game_state=connectfour.new_game()
    common_functions.welcome_user()
    common_functions.print_game_board(game_state.board)
    print()
    print("Game Started")
    print()
    
    run_step(game_state)  
  
if __name__=="__main__":
    main()
    
