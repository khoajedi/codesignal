def solution(time):
    h = int(time[:2])
    m = int(time[-2:])
    
    if h == 24 and m != 0:
        return False
        
    if h < 0 or h > 23:
        return False
        
    if m < 0 or m > 59:
        return False
        
    return True