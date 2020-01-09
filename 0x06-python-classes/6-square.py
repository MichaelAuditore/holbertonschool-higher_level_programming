#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.size == 0):
            print()
        else:
            pos = self.position[1]
            while (pos > 0):
                print()
                pos = pos - 1
            h, v = self.size, self.size
            for i in range(h):
                nspace = self.position[0]
                for j in range(v):
                    while(nspace > 0):
                        print("", end=" ")
                        nspace = nspace - 1
                    print("#", end="")
                print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        is_num = 0
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if not isinstance(i, int):
                    is_num = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
                elif i < 0:
                    is_num = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
            if is_num == 0:
                self.__position = value
