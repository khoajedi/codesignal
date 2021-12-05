def solution(inputArray):
    m = max(len(x) for x in inputArray)
    return list(x for x in inputArray if len(x) == m)

def solutionV2(inputArray):
    m = max(len(x) for x in inputArray)
    return [x for x in inputArray if len(x) == m]