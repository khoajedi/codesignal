def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    for (x, y) in zip(inputArray[1:], inputArray[2:]):
        prod = x * y
        if prod > max:
            max = prod
    return max