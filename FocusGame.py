# Author: Sam Silber
# Date: 11/14/20
# Description: A class to simulate a 2-player game of Focus, an abstract strategy board game

from Board import Board
from Player import Player

class FocusGame:
    """
    An instance of a 2-player game of Focus/Domination
    """

    def __init__(self, p1=("PlayerA", "R"), p2=("PlayerB", "G")):
        """
        Initialize a FocusGame object with tuples for each player's name and color as parameters;
        initialize the game board
        """

        # Create Player objects from the provided parameters
        self._p1 = Player(p1[0], p1[1])
        self._p2 = Player(p2[0], p2[1])

        # Create a dictionary for looking up players and their attributes
        self._players = {self._p1.get_player_name(): self._p1, self._p2.get_player_name(): self._p2}

        # Initialize so any player can make the first move
        self._player_turn = None

        # Initialize game board
        self._board = Board(self._p1, self._p2).get_board()

    def print_board(self):
        """
        Board printing function for debugging/testing
        """
        for i in self._board:
            print(i)

    def get_stack(self, coord=None):
        """
        Get the stack at the specified coordinates tuple-- taken as (row, column)
        """
        if coord is None:
            return None
        else:
            return self._board[coord[0]][coord[1]]

    def set_player_turn(self, player):
        """
        Set the player's turn to the provided player
        """
        self._player_turn = player

    def switch_player_turn(self):
        """
        Make it the other player's turn
        """
        if self._player_turn == self._p1.get_player_name():
            self.set_player_turn(self._p2.get_player_name())
        else:
            self.set_player_turn(self._p1.get_player_name())

    def get_player_from_name(self, player_name):
        """
        Returns the Player object from the name of the provided player
        """
        players = self._players
        if player_name in players:
            return players[player_name]
        return None

    def is_players_turn(self, player_name):
        """
        Check if it's the provided player's turn
        """

        # Set current player if it's the first turn
        # Then check if the player name matches the current value for player_turn
        if self._player_turn is None:
            self.set_player_turn(player_name)

        if player_name == self._player_turn:
            return True
        return False

    def is_valid_location(self, player_name, to_coord, from_coord=None):
        """
        Check if the to and from locations for a single or multiple move are valid
        From coord is optional to support this validation function for reserve moves
        """

        # Check if locations are inbounds
        try:
            to_stack = self.get_stack(to_coord)
            from_stack = self.get_stack(from_coord)

            # check if it's a reserve move
            if from_coord is None:
                return True

        except IndexError:
            return False

        # checks to make if it is a single or multiple move
        if from_coord is not None:

            # from_coord stack must not be empty
            if from_stack.is_empty():
                return False

            # from_coord stack must be owned by the player whose turn it is
            # (i.e., the player must have the top piece on the stack they are moving)
            player = self.get_player_from_name(player_name)
            color = player.get_color()
            if color != from_stack.peek():
                return False

            # to_coord and from_coord must be  in a straight line (horizontal or vertical)
            if (from_coord[0] != to_coord[0]) and (from_coord[1] != to_coord[1]):
                return False
            return True

    def is_valid_num_pieces(self, from_coord, to_coord, num_pieces):
        """
        Check if there are a valid number of pieces to complete the move
        """

        # if moving more pieces than are in the stack currently
        from_stack = self.get_stack(from_coord)
        if num_pieces > from_stack.get_length():
            return False

        # if there aren't enough pieces being moved to complete the move to the new location
        from_total = from_coord[0] + from_coord[1]
        to_total = to_coord[0] + to_coord[1]
        if (from_total + num_pieces != to_total) and (from_total - num_pieces != to_total):
            return False
        return True

    def add_to_stack(self, from_coord, to_coord, num_pieces):
        """
        Recursively add pieces from one stack to the top of another stack
        """
        from_stack = self.get_stack(from_coord)
        to_stack = self.get_stack(to_coord)

        if num_pieces == 0:
            return
        else:
            piece = from_stack.pop_from_index(num_pieces)
            to_stack.append(piece)
            self.add_to_stack(from_coord, to_coord, num_pieces - 1)

    def add_from_reserve(self, player_name, to_coord):
        """
        Add pieces from a player's reserve to the top of another stack
        """
        player = self.get_player_from_name(player_name)
        color = player.get_color()
        to_stack = self.get_stack(to_coord)

        to_stack.append(color)
        player.remove_from_reserve()

    def remove_from_stack(self, player_name, to_stack):
        """
        Remove pieces from the bottom of a stack if there are more than 5 pieces
        Add these pieces either to the player's reserve or captured pieces
        """
        player = self.get_player_from_name(player_name)
        color = player.get_color()

        while to_stack.get_length() > 5:
            piece = to_stack.popLeft()

            if piece == color:
                player.add_to_reserve()
            else:
                player.add_to_captured()

    def player_wins(self, player_name):
        """
        Assess whether the provided player wins the game by having captured 6 pieces
        """
        player = self.get_player_from_name(player_name)
        if player.get_captured() == 6:
            return True
        return False

    def move_piece(self, player_name, from_coord, to_coord, num_pieces):
        """
        Take player name, coordinates of the moves to/from location, and the number of pieces being moved, and
        then move the piece if possible. Handle if move is not possible (out of turn, not a location, etc)
        """

        if not self.is_players_turn(player_name):
            return "Not your turn"

        if not self.is_valid_location(player_name, to_coord, from_coord):
            return "Invalid location"

        if not self.is_valid_num_pieces(from_coord, to_coord, num_pieces):
            return "Invalid number of pieces"

        self.add_to_stack(from_coord, to_coord, num_pieces)

        if self.get_stack(to_coord).get_length() > 5:
            self.remove_from_stack(player_name, self.get_stack(to_coord))

        if self.player_wins(player_name):
            return "{} Wins".format(player_name)

        self.switch_player_turn()
        return "Successfully moved"

    def show_pieces(self, coord):
        """
        Takes a position on the board and returns a list showing the pieces that are present at that location
        with the bottom-most pieces at the 0th index of the array
        """
        return self._board[coord[0]][coord[1]].as_list()

    def show_reserve(self, player_name):
        """
        Shows the count of pieces that are in reserve for the provided player
        If no pieces are in reserve, return 0
        """
        player = self.get_player_from_name(player_name)
        return player.get_reserve()

    def show_captured(self, player_name):
        """
        Shows the number of pieces captured by the provided player
        If no pieces have been captured, return 0
        """
        player = self.get_player_from_name(player_name)
        return player.get_captured()

    def reserved_move(self, player_name, to_coord):
        """
        Places a piece from the reserve to the specified location
        Reduce the reserve pieces of that player by one and make appropriate adjustments to pieces at the location
        If there are no pieces in reserve, return 'no pieces in reserve'
        """
        if not self.is_players_turn(player_name):
            return "Not your turn"

        if not self.is_valid_location(player_name, to_coord):
            return "Invalid location"

        player = self.get_player_from_name(player_name)
        if player.get_reserve() == 0:
            return False

        self.add_from_reserve(player_name, to_coord)

        if self.get_stack(to_coord).get_length() > 5:
            self.remove_from_stack(player_name, self.get_stack(to_coord))

        if self.player_wins(player_name):
            return "{} Wins".format(player_name)

        self.switch_player_turn()
        return "Successfully moved"