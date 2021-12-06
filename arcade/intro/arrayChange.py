def solution(inputArray):
    sum = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            diff = inputArray[i-1] - inputArray[i] + 1
            sum += diff
            inputArray[i] += diff
    return sum