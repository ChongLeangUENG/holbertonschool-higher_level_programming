#!/usr/bin/python3
"""define a class square"""


class Square:
    """_summary_
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize the square object

        Args:
            size (int): size of the square, defaults to 0
        """
        self.__size = size
        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if type(position) is not tuple or len(position) != 2 or \
           type(position[0]) is not int or position[0] < 0 or \
           type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        seld.__position = value

    def area(self):
        """returns the square are of the object
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints a # square according to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
