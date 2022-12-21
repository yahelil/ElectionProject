from VoteManager import VoteManager as manager
from protocolEnv import Protocol as protocol
import socket
from Voter import Voter
from DoubleEnvelope import DoubleEnvelope
from quiter import Quiter

class VoteServer:
    def __init__(self):
        self.vote_manager = manager()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.voters_list = []

    # responsible for setting up the server, making it ready to accept clients
    def start(self):
        self.server_socket.bind((protocol.SERVER_IP, protocol.PORT))
        self.server_socket.listen()
        print(f"Server is ready for connections")

    @staticmethod
    def quitish():
        protocol.send_msg(client_socket, "finish")
        quit()

    # responsible for handling connections, receiving messages, and sending responses
    def accept_client(self):
        client_conn, addr = self.server_socket.accept()     # accepting the client
        print(f"Connected by {addr}")

        with client_conn:
            data = protocol.receive_binary(client_conn)     # receiving the first message (object)
            # checking if data is valid
            if data[0]:  # data is a tuple (is valid, actual data)
                # check what instance data is and react to that
                if isinstance(data[1], Voter):
                    # the object received is a voter
                    second_data = protocol.receive_binary(client_conn)  # receiving the envelope
                    if second_data[0]:  # the second data is valid
                        self.vote_manager.envelope_handler(second_data[1])  # handle it via the vote manager
                        self.voters_list.append(data[1])    # count the voter

                elif isinstance(data[1], DoubleEnvelope):
                    # the object received is a double envelope
                    if data[1].voter not in self.voters_list:   # if the voter hasn't voted yet
                        self.vote_manager.envelope_handler(data[1])     # handle it via the vote manager
                        self.voters_list.append(data[1].voter)  # count the voter
                elif isinstance(data[1], Quiter):
                    self.vote_manager.results()
                    quitish()
        client_conn.close()
        print(f"disconected {client_conn}")
        self.accept_client()    # redo that whole process


if __name__ == '__main__':
    server = VoteServer()
    server.start()
    server.accept_client()
