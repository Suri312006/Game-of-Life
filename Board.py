import unit
def __init__(self, row = 10, col = 10):
    self.units = None
    for r in range(row):
        for c in range(col):
            self.units[r][c] = unit()