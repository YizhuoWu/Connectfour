"""
ICS32 Project 2
Navigator: Wenyu Ouyang ID:23402729
Driver:Yizhuo Wu ID:14863527
"""

import socket
import common_functions
import connectfour
import I32CFSP_and_all_socket

def _get_IP():
    '''
    This function will ask the user for an IP address that they want to connect to.
    '''
    while True:
        IP_address=input("Enter the IP_Address you want to connect to: ")
        if ' ' not in IP_address or IP_address != '': 
            return IP_address
        print("An IP_address cannot be empty!")
    

def _get_port():
    '''
    This function will ask the user for the port number that they want to connect to.
    '''
    
    while True:
        try:
            port=int(input("Enter the port you want to connect to:"))
            if port != '' and 0 < port < 65535:
                return port
            print("The port number should between 0 and 65535 and can't be empty")    
        except ValueError:
            print("Please enter a number.")
    

def _get_user_name()->None:
    '''
    This function asks the user for a username, if the username is invalid, the program
    will ask the user to enter again until it is a valid username.
    '''
    while True:
        user_name=input("Please enter a username you want: ").strip()
        if " " not in user_name:
            return user_name
        print("This is an invalid username, please try again!")
       

def _get_ready(ourconnection)->None:
    '''
    This function will make sure everything is fine before the game start. It will sent the
    username to the server and get response, if the response startswith 'WELCOME', the program
    will sent the request for an AI_Game and once it received 'READY' from the server, the game
    will start.
    '''
    username=_get_user_name()
    I32CFSP_and_all_socket.write_to_the_server(ourconnection,"I32CFSP_HELLO "+username) 
    response=I32CFSP_and_all_socket.read_line_from_server(ourconnection)
    if response.startswith("WELCOME "):
        print(response)
        I32CFSP_and_all_socket.write_to_the_server(ourconnection,"AI_GAME")
        if I32CFSP_and_all_socket.read_line_from_server(ourconnection)=="READY":
            pass
                
    elif response.startswith('NO_USER '):
        print("NO_USER")
   
def _user_turn(ourconnection):
    '''
    If it is user's turn, the function will get the user's action(drop or pop) and the column
    number, thenm sent them to the server.
    '''
    print("It's your turn now.")
    print()
    cmd=common_functions.get_user_cmd()
    column_number=common_functions.get_col_number()
    I32CFSP_and_all_socket.write_to_the_server(ourconnection,cmd.upper()+" "+str(column_number+1))
    return cmd,column_number
    
def _ai_turn(ourconnection):
    '''
    If it is ai's turn, the function will receive the command from the server and print them out,
    then pass the command from the server to other functions.If the command given by the server is
    invalid, the _run_whole_game function will prompt the server to enter the valid command. However,
    the server will send 'READY' to client instead of a valid command. So if the program detects that
    the command is unable to split into two commands,(which means the server gave an invalid command before)
    the program will end.
    '''
    print("Now AI is thinking")
    print()

    I32CFSP_and_all_socket.read_line_from_server(ourconnection)
    computer_cmd=I32CFSP_and_all_socket.read_line_from_server(ourconnection)
    
    print("AI wants to "+computer_cmd)
    I32CFSP_and_all_socket.read_line_from_server(ourconnection)
    print()
    try:
        cmd=computer_cmd.split()[0]
    except IndexError:
        exit()
    column_number=int(computer_cmd.split()[1])-1
    return cmd,column_number
      
def _run_whole_game(game_state,ourconnection)->None:
    '''
    This function will run the game steps. First, it checks whether the game is over(If there is
    a winner). If not, then it checks who's turn at that moment should be. If it's user's turn, it
    will get the command and column number from the user. If it's AI's turn, it will get them from
    the server. Then it will proceed the command, if the command is 'drop', it will run the drop
    function and print the board to the user. If the command is 'pop', it will run the pop
    function and print the board to the user. When one of the player won, it print the congratulations
    message and end the game.
    '''
    if connectfour.winner(game_state)==connectfour.NONE:
        if game_state.turn==1:
            cmd,column_number=_user_turn(ourconnection)
        elif game_state.turn==2:
            cmd,column_number=_ai_turn(ourconnection)

        try:
            if cmd.upper()=='DROP':
                new_game_state=connectfour.drop(game_state,column_number)
                common_functions.print_game_board(new_game_state.board)
                _run_whole_game(new_game_state,ourconnection)
           
            elif cmd.upper()=="POP":
                new_game_state=connectfour.pop(game_state,column_number)
                common_functions.print_game_board(new_game_state.board)
                _run_whole_game(new_game_state,ourconnection)
                
        except connectfour.InvalidMoveError:
            print()
            print("Invalid Move! Please try again!")
            print()
            _run_whole_game(game_state,ourconnection)

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
    The main function will firstly make a new game and welcomes the user. Then it will get the
    IP_address and port number from the user and try to connect, if it cannot connect to the server,
    an error message will be print and end the program. If it successfully connect to the server, it
    will check whether everything is ok to start the game. If so, it will run the whole game until a
    winner is occur.
    '''
    game_state=connectfour.new_game()

    common_functions.welcome_user()

    IP_address=_get_IP()

    port=_get_port()

    try:
        ourconnection=I32CFSP_and_all_socket.connect(IP_address,port)

    except TimeoutError and socket.gaierror:

        print("There is an error when connecting to the server, no reply sent from the server."+
              "Please check that you entered the correct IP address and port number.")
        return 
    
    _get_ready(ourconnection)

    common_functions.print_game_board(game_state.board)

    print()
    print("Game Started")
    print()

    _run_whole_game(game_state,ourconnection)

    I32CFSP_and_all_socket.close(ourconnection)
  
if __name__=="__main__":
    main()
    




        
        
        
