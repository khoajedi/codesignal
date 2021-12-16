def solution(n):
    for c in str(n):
        if int(c) % 2 != 0:
            return False
    
    return True