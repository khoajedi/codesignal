def solution(inputArray):
    m = max(len(x) for x in inputArray)
    return list(x for x in inputArray if len(x) == m)