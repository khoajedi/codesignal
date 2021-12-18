def solution(inputString):
    s = string.ascii_lowercase
    d = {k:0 for k in s}
    
    for c in inputString:
        d[c] += 1
        
    for i in range(1, len(s)):
        if d[s[i]] > d[s[i - 1]]:
            return False
            
    return True