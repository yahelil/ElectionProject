from quiter import Quiter
import socket
from protocolEnv import Protocol as p


class quitting_client:
    def __init__(self):
        self.quitting_Socket = socket.socket()

    # responsible to connecting the calpi to the main server
    def connect(self):
        self.quitting_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.quitting_Socket.connect((p.SERVER_IP, p.PORT))

    @staticmethod
    def generate_new_quiter():
        return Quiter()

    def main(self):
        self.connect()
        p.send_binary(self.quitting_Socket, self.generate_new_quiter())


if __name__ == "__main__":
    app = quitting_client()
    app.main()
