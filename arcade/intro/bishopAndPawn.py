def solution(bishop, pawn):
    a = abs(ord(bishop[0]) - ord(pawn[0]))
    b = abs(int(bishop[1]) - int(pawn[1]))
    return a == b