def solution(st):
    if checkPalidrome(st):
        return st
        
    for i in range(1, len(st)):
        ns = st + st[:i][::-1]
        print(ns)
        if checkPalidrome(ns):
            return ns
    
def checkPalidrome(st):
    return st == st[::-1]