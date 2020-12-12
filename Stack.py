# Author: Sam Silber
# Date: 11/14/20
# Description: A class to represent a stack of game pieces in Focus, an abstract strategy board game

class Stack:
    """
    Implement a double-ended queue ADT ("deque") to represent stacks of game pieces on the Focus board
    """

    def __init__(self, color):
        """
        Initialize a stack object with its starting color
        """
        self._list = [color]

    def append(self, data):
        """
        Add an item to the top (right) of the stack
        """
        self._list.append(data)

    def pop_from_index(self, index):
        """
        Delete and return the item at a specified part of the stack
        The index is relative to the top (right) of the stack
        """
        val = self._list[index * -1]
        del self._list[index * -1]
        return val

    def popLeft(self):
        """
        Delete and return the item at the bottom (left) of the stack
        """
        val = self._list[0]
        del self._list[0]
        return val

    def peek(self):
        """
        Return the top (right) item in the stack
        """
        return self._list[-1]

    def get_length(self):
        """
        Return the length of a stack (i.e., the number of items in the stack)
        """
        return len(self._list)

    def as_list(self):
        """
        Return the length stack as a list with the bottom item in the 0th element
        """
        return self._list

    def is_empty(self):
        """
        Boolean to determine whether the stack is empty
        """
        return len(self._list) == 0

    def __repr__(self):
        """
        String representation for board printing/debugging
        Show a "tuple" with the color at the top of the stack and the number of items in the stack
        """
        if self.get_length() >= 1:
            return "(" + str(self.peek()) + ", " + str(self.get_length()) + ")"
        else:
            return "(0, 0)"
