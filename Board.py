from Validation import Validation
from BoxName import BoxName

import random

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


class Board:
    def __init__(self):
        self.board = board

    def generateBoard(self, filled):
        i = 0
        while i < filled:
            number = random.randrange(1, 10)
            x = random.randrange(0, 9)
            y = random.randrange(0, 9)
            valid = Validation(self.board)
            if valid.valid(number, x, y):
                self.board[x][y] = number
                i += 1

    def printBoard(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def addNumber(self, number, x, y):
        valid = Validation(self.board)
        if not valid.isZero(x, y):
            print('- - - - - - - - - - - - - ')
            print('- CANNOT MODIFY THIS FIELD - ')
            print('- - - - - - - - - - - - - ')
            return self.printBoard()
        elif not valid.validRow(number, x):
            print('- - - - - - - - - - - - - ')
            print('- NUMBER EXIST IN ROW ' + str(x) + ' - ')
            print('- - - - - - - - - - - - - ')
            return self.printBoard()
        elif not valid.validColumn(number, y):
            print('- - - - - - - - - - - - - ')
            print('- NUMBER EXIST IN COLUMN ' + str(y) + ' - ')
            print('- - - - - - - - - - - - - ')
            return self.printBoard()
        elif not valid.validBox(number, x, y):
            boxName = BoxName()
            print('- - - - - - - - - - - - - ')
            print('- NUMBER EXIST IN ' + boxName.show(x // 3, y // 3) + ' - ')
            print('- - - - - - - - - - - - - ')
            return self.printBoard()
        elif not valid.valid(number, x, y):
            self.board[x][y] = number
            print('- - - - - - - - - - - - - ')
            print('- - - - -  NEW  - - - - - ')
            print('- - - - - - - - - - - - - ')
            return self.printBoard()

    def isWin(self):
        if not any(0 in sublist for sublist in self.board):
            return True
        else:
            return False

    def getNumber(self):
        number = 1
        try:
            number = int(input('Enter number which you want to add: '))
        except ValueError:
            print("Number must be 1-9")
            number = self.getNumber()
        finally:
            if number < 1 or number > 9:
                print("Number must be 1-9")
                number = self.getNumber()

        return number

    def getRow(self):
        row = 1
        try:
            row = int(input('Enter row which you want to add: '))
        except ValueError:
            print("Row must be 1-9")
            row = self.getRow()
        finally:
            if row < 1 or row > 9:
                print("Row must be 1-9")
                row = self.getRow()

        return row

    def getColumn(self):
        column = 1
        try:
            column = int(input('Enter column which you want to add: '))
        except ValueError:
            print("Column must be 1-9")
            column = self.getColumn()
        finally:
            if column < 1 or column > 9:
                print("Column must be 1-9")
                column = self.getColumn()

        return column

    def play(self):
        number = self.getNumber()
        row = self.getRow() - 1
        column = self.getColumn() - 1
        self.addNumber(number, row, column)
        if self.isWin():
            print('YOU WON!!!')
        else:
            self.play()
