"""
    ------------------------------
            Envelope.py
    ------------------------------

    this file implements the class 'Envelope'
    that class represents an envelope.

    it has 1 properties:
        notes -> a list of notes, type list

    it has 2 methods:
        is_valid() -> returns whether the envelope is considered valid
        status() -> returns a tuple (v, n),
            where v is a bool (whether the envelope is valid)
            and n is a note containing the name of the party
"""


class Envelope:
    def __init__(self, notes):
        self.notes = notes

    # returns a bool (is the envelope valid?)
    def is_valid(self):
        if 0 <= len(self.notes) < 5 and len(set(self.notes)) == 1:
            # is the list made of out the same note n times
            # where n is in [0, 5)
            return True

        return False

    # returns a tuple containing a bool (is the envelope valid?)
    # and a note (the note containing the chosen party)
    def status(self):
        if self.is_valid():     # if valid
            if len(self.notes) == 0:           # and empty
                return True, "Empty"  # Empty Envelope
            return True, self.notes[0]  # Valid and election_note
        else:
            return False, None  # invalid envelope
