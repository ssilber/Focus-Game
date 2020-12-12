# Author: Sam Silber
# Date: 11/14/20
# Description: A class representing a player in a game of Focus, an abstract strategy board game

class Player:
    """
    Represents a player in Focus
    """

    def __init__(self, player_name, color):
        """
        Initialize a Player object with data members for the provided player's name and color of their game piece;
        instantiate a player's reserve game piece and captured game piece count at 0
        """
        self._player_name = player_name
        self._color = color
        self._reserve = 0
        self._captured = 0

    def get_player_name(self):
        """
        Return the name of the player
        """
        return self._player_name

    def get_color(self):
        """
        Return the color of the player's game piece
        """
        return self._color

    def get_reserve(self):
        """
        Get the count of pieces in the player's reserve
        """
        return self._reserve

    def get_captured(self):
        """
        Get the count of pieces a player has captured
        """
        return self._captured

    def add_to_reserve(self):
        """
        Increment the number of pieces in a player's reserve by 1
        """
        self._reserve += 1

    def remove_from_reserve(self):
        """
        Decrement the number of pieces in a player's reserve by 1
        """
        self._reserve -= 1

    def add_to_captured(self):
        """
        Increment the number of pieces a player has captured by 1
        """
        self._captured += 1
