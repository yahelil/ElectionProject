import pickle
import socket

"""
    ------------------------------
            protocolEnv.py
    ------------------------------

    this file implements the class 'Protocol'

    the file implements 4 properties:
        candidates -> the list of all the parties
        length_field_size -> the size of the header at any given message
        SERVER_IP -> the ip address of the computer that's running the server
        PORT -> the port sockets will listen to

    it has 2 methods:
        change_to_binary(obj) ->
            takes an object (any class) and returns that same object in binary (b string)
            
        change_to_class(bytes_obj) ->
            takes a binary string (b string), and returns the object it describes (any class)
            
        send_binary(my_socket, msg) ->
            responsible for sending objects via sockets
            takes 2 params: my_socket (socket), msg (any class)
        
        receive_binary(my_socket) ->
            responsible for receiving objects via sockets
            takes 1 params: my_socket (socket)
            returns a tuple(bool did succeed?, object)
            
        send_msg(my_socket, msg) ->
            responsible for sending messages via sockets
            takes 2 params: my_socket (socket), msg (string)
            
        get_msg(my_socket) ->
            responsible for receiving messages via sockets
            takes 1 params: my_socket (socket)
            returns a string that represents the received message
"""


class Protocol:
    candidates = ["red", "blue", "green", "yellow"]     # the list of all the parties
    length_field_size = 5   # the size of the header at any given message
    SERVER_IP = "127.0.0.1"     # the ip address of the computer that's running the server
    PORT = 80   # the port sockets will listen to

    @staticmethod
    # takes an object and returns that same object in binary
    def change_to_binary(obj):
        return pickle.dumps(obj)

    @staticmethod
    # takes a binary string, and returns the object it describes
    def change_to_class(bytes_obj):
        return pickle.loads(bytes_obj)

    @staticmethod
    # responsible for sending objects via sockets
    def send_binary(my_socket, msg):
        # msg contains the object
        msg = Protocol.change_to_binary(msg)    # msg is that same object, but in binary
        length = str(len(msg))  # length is a string containing the length of the binary string
        Protocol.send_msg(my_socket, length)    # sending the length
        my_socket.send(msg)     # sending the object in binary

    @staticmethod
    # responsible for receiving objects via sockets
    # returns a tuple(bool did succeed?, object)
    def receive_binary(my_socket):
        try:
            while True:
                try:
                    length = Protocol.get_msg(my_socket)    # receive the length of the binary object
                    return True, Protocol.change_to_class(my_socket.recv(int(length)))  # return succeeded, the object

                except socket.timeout:
                    pass

        except (ValueError, TypeError):     # didn't receive the length properly
            return False, ""    # return not succeeded, (None)

    @staticmethod
    # responsible for sending messages via sockets
    def send_msg(my_socket, msg):
        # creates a message from the form: header + message
        #                   header:
        # n digits are allocated towards the length of the message
        # n being 'length_field_size'
        msg = str(len(msg)).zfill(Protocol.length_field_size) + msg # create the header and concat it with the content
        my_socket.send(msg.encode())    # send that message

    @staticmethod
    # responsible for receiving messages via sockets
    # returns a string that represents the received message
    def get_msg(my_socket):
        try:
            # receive the header and get the length of the content
            length = my_socket.recv(Protocol.length_field_size).decode()

            if length == '':
                raise socket.timeout

            data_left = int(length)     # set the length of unread data to the length of the content
            data_recv = b''  # here the received content will bw stored
            if data_left > 0:   # if there are more unread characters at the content of the message
                data_recv += my_socket.recv(data_left)  # read those
            return data_recv.decode()   # return the received data in a form of a string
        except ValueError or TypeError:     # wasn't able to extract the length of the content from the header
            return None # return None (couldn't parse the message)

