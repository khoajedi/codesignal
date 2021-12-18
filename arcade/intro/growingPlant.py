def solution(upSpeed, downSpeed, desiredHeight):
    height = 0
    day = 0
    
    while height < desiredHeight:
        day += 1
        height += upSpeed
        
        if height >= desiredHeight:
            return day
            
        height -= downSpeed