def solution(text):
    a = []
    s = ""
    
    for c in text:
        if c.isalpha():
            s += c
        else:
            a.append(s)
            s = ""
    
    a.append(s)
    s = ""
    
    m = max(len(e) for e in a)
    
    for e in a:
        if len(e) == m:
            return e