def solution(inputArray):
    stride = 2
    coor = stride
    dest = max(inputArray)
    
    while coor <= dest:
        if coor in inputArray:
            stride += 1
            coor = stride
            continue
        coor += stride
        
    return stride