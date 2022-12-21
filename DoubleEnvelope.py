from Voter import Voter
"""
    ----------------------------------
            DoubleEnvelope.py
    ----------------------------------

    this file implements the class 'DoubleEnvelope'
    that class represents an envelope that's inside of an envelope.
    
    it has 2 properties:
        envelope -> represents the inner envelope, type envelope
        voter -> represents the one who's envelope this is, type voter
"""


class DoubleEnvelope:
    def __init__(self, envelope, voter):
        self.envelope = envelope
        self.voter = voter
