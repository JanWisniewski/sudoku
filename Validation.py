class Validation:
    def __init__(self, board=[]):
        self.board = board

    def valid(self, number, x, y):
        return self.isZero(x, y) and \
               self.validRow(number, x) and \
               self.validColumn(number, y) and \
               self.validBox(number, x, y)

    def isZero(self, x, y):
        if self.board[x][y] == 0:
            return True
        else:
            return False

    def validRow(self, number, x):
        for i in range(len(self.board[x])):
            if self.board[x][i] == number:
                return False
        return True

    def validColumn(self, number, y):
        for i in range(len(self.board)):
            if self.board[i][y] == number:
                return False
        return True

    def validBox(self, number, x, y):
        box_x = x // 3
        box_y = y // 3

        for i in range(box_y * 3, box_y * 3 + 2):
            for j in range(box_x * 3, box_x * 3 + 2):
                if self.board[i][j] == number:
                    return False

        return True
