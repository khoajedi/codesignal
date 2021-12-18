def solution(n):
    c = 0
    
    while n >= 10:
        c += 1
        n = sum(int(d) for d in str(n))
        
    return c