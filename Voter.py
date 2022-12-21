"""
    ------------------------------
            Voter.py
    ------------------------------

    this file implements the class 'Voter'
    that class represents a clump of information about a person who has voted.

    it has 2 properties:
        _id -> the id number of that person
        name -> the name of that person

"""


class Voter:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name
