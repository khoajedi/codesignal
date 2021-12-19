def solution(inputString):
    s = inputString.split("-")
    
    if len(s) != 6:
        return False
        
    for e in s:
        if len(e) != 2:
            return False
    
    return all(e[0] in string.hexdigits and e[1] in string.hexdigits for e in s)