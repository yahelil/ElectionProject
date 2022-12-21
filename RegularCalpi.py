from protocolEnv import Protocol as p
import socket
from Voter import Voter
from Note import Note
from Envelope import Envelope


class Calpi1:
    def __init__(self):
        self.voters = dict()
        self.votes = []
        self.socket = None
        self.is_working = True

    @staticmethod
    # displays all the candidates
    def display_candidates():
        print(p.candidates)

    # responsible to connecting the calpi to the main server
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((p.SERVER_IP, p.PORT))
        self.socket.settimeout(0.2)

    @staticmethod
    # takes a vote (string) as a param
    # returns whether the vote is valid or not
    def is_valid(vote):
        return vote in p.candidates

    def terminated(self):
        try:
            p.get_msg(self.socket)
            return True

        except socket.timeout:
            return False
    # the main method, responsible for voting,
    # and sending the information gathered at the voting process
    def collect_votes(self):
        # getting the voter's info and building voters dictionary
        while self.is_working:
            _id = input("Enter ID: ")
            name = input("Enter your name: ")
            voter = Voter(_id, name)
            self.voters.update({_id: voter})

            # displaying the candidates
            print(f"Now you can vote!\nYou can vote to one of these:{self.display_candidates()}\n[type exit to stop]")

            # voting process
            while (vote := input("ENTER YOUR VOTE: ").lower()) != "exit":
                if vote in p.candidates:
                    self.votes.append(vote)
                else:
                    print("your vote isn't valid, vote again")

            # validate
            self.connect()

            if len(self.votes) and self.is_valid(self.votes[-1]):
                envelope = Envelope([Note(i) for i in self.votes])
                if envelope.status()[0]:
                    p.send_binary(self.socket, voter)  # send the voter to the server
                    p.send_binary(self.socket, envelope)  # send the envelope to the server
            self.votes = []  # self.votes is a list per person
            if self.terminated():
                quit()


if __name__ == '__main__':
    calpi = Calpi1()
    calpi.collect_votes()
