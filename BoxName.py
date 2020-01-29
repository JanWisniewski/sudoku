class BoxName:
    def show(self, x, y):
        boxName = ''
        if x == 0:
            boxName += 'TOP '
        elif x == 1:
            boxName += 'MIDDLE '
        elif x == 2:
            boxName += 'BOTTOM '
        if y == 0:
            boxName += 'LEFT'
        elif y == 1:
            boxName += 'MIDDLE'
        elif y == 2:
            boxName += 'RIGHT'
        if x == 1 and y == 1:
            boxName = 'CENTRAL'
        boxName += ' BOX'
        return boxName
