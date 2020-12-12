# Author: Sam Silber
# Date: 11/14/20
# Description: A class representing the board in a game of Focus, an abstract strategy board game

from Stack import Stack

class Board:
    """
    Represents a Board for the game of Focus
    """
    def __init__(self, p1, p2):
        """
        Initialize a Board object with parameters for 2 Player objects
        """

        # Create Player objects from the provided parameters
        self._p1 = p1
        self._p2 = p2

        # Initialize game board as a 6x6 list of lists, with each slot containing a Stack object created
        # using the color data members from the Player objects
        self._board = [
            [Stack(self._p1.get_color()), Stack(self._p1.get_color()), Stack(self._p2.get_color()),
             Stack(self._p2.get_color()),
             Stack(self._p1.get_color()), Stack(self._p1.get_color())],
            [Stack(self._p2.get_color()), Stack(self._p2.get_color()), Stack(self._p1.get_color()),
             Stack(self._p1.get_color()),
             Stack(self._p2.get_color()), Stack(self._p2.get_color())],
            [Stack(self._p1.get_color()), Stack(self._p1.get_color()), Stack(self._p2.get_color()),
             Stack(self._p2.get_color()),
             Stack(self._p1.get_color()), Stack(self._p1.get_color())],
            [Stack(self._p2.get_color()), Stack(self._p2.get_color()), Stack(self._p1.get_color()),
             Stack(self._p1.get_color()),
             Stack(self._p2.get_color()), Stack(self._p2.get_color())],
            [Stack(self._p1.get_color()), Stack(self._p1.get_color()), Stack(self._p2.get_color()),
             Stack(self._p2.get_color()),
             Stack(self._p1.get_color()), Stack(self._p1.get_color())],
            [Stack(self._p2.get_color()), Stack(self._p2.get_color()), Stack(self._p1.get_color()),
             Stack(self._p1.get_color()),
             Stack(self._p2.get_color()), Stack(self._p2.get_color())]
        ]

    def get_board(self):
        """
        Return the board as a list of lists
        """
        return self._board

