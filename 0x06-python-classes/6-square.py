#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            pos = self.position[1]
            while (pos > 0):
                print()
                pos -= 1
            x, y = self.size, self.size
            for i in range(x):
                nspaces = self.position[0]
                for j in range(y):
                    while(nspaces > 0):
                        print("", end=" ")
                        nspaces -= 1
                    print("#", end="")
                print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            if isinstance(value, int) and value >= 0:
                self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        is_num = True
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for val in value:
                if not isinstance(val, int) or val < 0:
                    is_num = False
                    raise TypeError("position must be a tuple of 2 " +
                                    "positive integers")
                    if is_num:
                        self.__position = value
