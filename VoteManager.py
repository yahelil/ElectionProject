from protocolEnv import Protocol as p
from Envelope import Envelope
from DoubleEnvelope import DoubleEnvelope


class VoteManager:
    """
    Vote Manager manage the vote.
    Manage the Calpis
    Counting
    """
    def __init__(self):
        self.votes = {candidate: 0 for candidate in p.candidates}
        self.votes.update({"Empty": 0})
        self.double_envelope_list = []

    # this method counts the votes, counts only the valid votes
    def count_note(self, envelope):
        envelope_status, envelope_note = envelope.status()
        if envelope_status:
            self.votes[envelope_note.name] += 1
            self.results()
        else:
            print("Envelope is not valid")

    # gets an envelope and count it using count_note. also checks if the envelope is from class envelope
    def envelope_handler(self, envelope):
        if isinstance(envelope, Envelope):
            return self.count_note(envelope)

        elif isinstance(envelope, DoubleEnvelope):
            self.double_envelope_list.append(envelope)

        else:
            print("Unknown envelope")
        return False

    def results(self):
        print(f"The results have been updated.\nHere are the results until now:")
        for key, value in self.votes.items():
            print(key, value)
