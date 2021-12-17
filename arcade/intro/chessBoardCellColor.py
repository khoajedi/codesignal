def solution(cell1, cell2):
    a = ord(cell1[0]) - ord(cell2[0])
    b = int(cell1[1]) - int(cell2[1])
    return (a + b) % 2 == 0