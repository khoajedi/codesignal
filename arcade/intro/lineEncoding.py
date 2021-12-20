def solution(s):
    letter = s[0]
    count = 0
    result = ""
    
    for c in s:
        if c == letter:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += letter
            letter = c
            count = 1
            
    if count > 1:
        result += str(count)
    result += letter
            
    return result