def solution(inputArray):
    m = 0
    for x, y in zip(inputArray[:-1], inputArray[1:]):
        m = max(m, abs(x - y))
    return m