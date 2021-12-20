def solution(inputString):
    result = ""
    
    for c in inputString:
        if c.isdigit():
            result += c
        else:
            return result
    
    return result