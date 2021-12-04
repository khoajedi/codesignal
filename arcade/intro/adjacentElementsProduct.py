def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    for (x, y) in zip(inputArray[1:], inputArray[2:]):
        prod = x * y
        if prod > max:
            max = prod
    return max

def solutionV2(inputArray):
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))