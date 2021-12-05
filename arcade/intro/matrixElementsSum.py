def solution(matrix):
    sum = 0
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            if matrix[x][y] == 0:
                break
            sum += matrix[x][y]
    return sum