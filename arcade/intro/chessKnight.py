def solution(cell):
    return sum(checkMove(move) for move in knightMoves(cell))
    
def knightMoves(cell):
    moves = []
    
    for i in (-1, 1):
        for j in (-2, 2):
            move = chr(ord(cell[0]) + i) + str(int(cell[1]) + j)
            moves.append(move)
            move = chr(ord(cell[0]) + j) + str(int(cell[1]) + i)
            moves.append(move)

    return moves        
    
def checkMove(move):
    if len(move) != 2:
        return False
    
    if ord(move[0]) < ord("a") or ord(move[0]) > ord("h"):
        return False
        
    if int(move[1]) < 1 or int(move[1]) > 8:
        return False
        
    return True