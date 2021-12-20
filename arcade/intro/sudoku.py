def solution(grid):
    return checkRows(grid) and checkCols(grid) and checkBoxes(grid)

def checkRows(grid):
    for row in grid:
        if set(row) != set(range(1, 10)):
            return False
    return True
    
def checkCols(grid):
    for col in zip(*grid):
        if set(col) != set(range(1, 10)):
            return False
    return True
    
def checkBoxes(grid):
    for i in (1, 4, 7):
        for j in (1, 4, 7):
            s = set()
            for k in (-1, 0, 1):
                for l in (-1, 0, 1):
                    s.add(grid[i+k][j+l])
            if s != set(range(1, 10)):
                return False
    return True