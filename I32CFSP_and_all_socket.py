"""
ICS32 Project 2
Navigator: Wenyu Ouyang ID:23402729
Driver:Yizhuo Wu ID:14863527
"""

import socket
from collections import namedtuple

'''
Create our connection via socket by using a namedtuple. 
'''
ourconnection = namedtuple(
    'ourconnection',
    ['socket', 'input', 'output'])

def connect(host:str,port:int)->ourconnection:
    '''
    This function will connect to the server using the socket.
    It will return the socket obejcet.(ourconnection)
    '''
    our_socket=socket.socket()
    
    our_socket.connect((host,port))

    our_input=our_socket.makefile('r')
    our_output=our_socket.makefile('w')

    return ourconnection(
        socket=our_socket,
        input=our_input,
        output=our_output)

def write_to_the_server(ourconnection,line:str)->None:
    '''
    This function will write data made by the user to
    the server.
    '''
    ourconnection.output.write(line+'\r\n')
    ourconnection.output.flush()

def read_line_from_server(ourconnection)->str:
    '''
    This function will receive the data from the server.
    '''

    line=ourconnection.input.readline()[:-1]
    return line

def close(ourconnection)->None:
    '''
    This function will close the connection between the client and
    server after playing the game.
    '''
    ourconnection.input.close()
    ourconnection.output.close()
    ourconnection.socket.close()
