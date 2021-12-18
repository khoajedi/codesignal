def solution(inputArray, k):
    base = sum(inputArray[:k])
    result = base
    
    for i in range(k, len(inputArray)):
        base += inputArray[i] - inputArray[i-k]
        result = max(result, base)
        
    return result