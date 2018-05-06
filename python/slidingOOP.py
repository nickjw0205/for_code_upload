# Sliding Puzzle
import random
import math

class Reader:
    @staticmethod
    def get_number(size):
        num = input("Type the number you want to move (Type 0 to quit): ")
        while not (num.isdigit() and 0 <= int(num) <= size * size - 1):
            num = input("Type the number you want to move (Type 0 to quit): ")
        return int(num)

class SlidingBoard:
    @staticmethod
    def create_board(numbers):
        size = int(math.sqrt(len(numbers)))
        board = []
        for i in range(size):
            k = i * size
            board.append(numbers[k : k+size])
        return board

    @staticmethod
    def create_init_board(size):
        numbers = list(range(size * size))
        random.shuffle(numbers)
        return SlidingBoard.create_board(numbers)

    @staticmethod
    def create_goal_board(size):
        numbers = list(range(size * size))
        numbers = numbers[1:]
        numbers.append(0)
        return SlidingBoard.create_board(numbers)

    def __init__(self,size):
        self.__board = SlidingBoard.create_init_board(size)
        self.__empty = self.find_position(0)

    @property
    def board(self):
        return self.__board

    def print_board(self):
        for row in self.__board:
            for item in row:
                if item == 0:
                    print("  ", end=" ")
                else:
                    print(str(item).rjust(2), end=" ")
            print()

    def find_position(self, num):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                if num == self.__board[i][j]:
                    return (i, j)

    def move(self, pos):
        (i, j) = pos
        if self.__empty == (i-1, j) or self.__empty == (i+1, j) or \
           self.__empty == (i, j-1) or self.__empty == (i, j+1):
            self.__board[self.__empty[0]][self.__empty[1]] = self.__board[i][j]
            self.__board[i][j] = 0
            self.__empty = pos
        else:
            print("Can't move! Try again.")

class SlidingPuzzleController():
    def __init__(self,size):
        self.__slider = SlidingBoard(size)
        self.__goal = SlidingBoard.create_goal_board(size)
        self.__size = size

    def play(self):
        while True:
            self.__slider.print_board()
            if self.__slider.board == self.__goal: 
                print("Congratulations!")
                break
            num = Reader.get_number(self.__size)
            if num == 0: 
                break
            pos = self.__slider.find_position(num)
            empty = self.__slider.move(pos)
        print("Please come again.")

if __name__ == "__main__": 
    import sys
    size = sys.argv[1]
    if size.isdigit() and int(size) > 1:
        SlidingPuzzleController(int(size)).play()
    else:
        print("Not a proper system argument.")