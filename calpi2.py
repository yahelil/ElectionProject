from protocolEnv import Protocol
from DoubleEnvelope import DoubleEnvelope
from Envelope import Envelope
from Voter import Voter
import socket


class Calpi2:
    def __init__(self):
        self.voter_list = []
        self.votes = []

    def collect_votes(self):
        self.calpi_socket = socket.socket()
        self.calpi_socket.connect((Protocol.SERVER_IP, Protocol.PORT))
        while True:

            print("welcome to calpi 2! we are like calpi 1 but with wierd rules!")
            print("your id_number?")
            id_number = input()
            if not type(id_number) == type(1):
                print("please enter a number")
            name = input("Your name:")
            if name == "exit":
                Protocol.send_msg(calpi_socket, "finnish")
                break
            vote = ""

            a = []
            while vote != "exit":
                print("what notes do u put in your envelope? you can vote only for one person")
                print('enter "exit" to to leave')
                print(f"You may vote to any of these candidates:{Protocol.candidates}")
                vote = input("Your vote:")
                if vote == "exit":
                    continue
                if vote in Protocol.candidates:
                    a.append(vote)
            voter = Voter(id_number, name)
            self.voter_list.append(voter)
            double_env = DoubleEnvelope(Envelope(a), voter)
            Protocol.send_binary(self.calpi_socket, double_env)
        self.calpi_socket.close()


if __name__ == "__main__":
    calpi = Calpi2()
    calpi.collect_votes()
