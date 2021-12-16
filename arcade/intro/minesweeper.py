def solution(matrix):
    width = len(matrix[0])
    height = len(matrix)
    
    box = []
    for i in range(height):
        local = []
        for j in range(width):
            x = [i-1] * 3 + [i] * 3 + [i+1] * 3
            y = [j-1, j, j + 1] * 3
            del x[4]
            del y[4]
            
            z = []
            for k in range(len(x)):
                if x[k] < 0 or y[k] < 0 or x[k] >= height or y[k] >= width:
                    z.append(k)
                    
            for k in z[::-1]:
                del x[k]
                del y[k]
            
            sum = 0
            
            for k in range(len(x)):
                sum += matrix[x[k]][y[k]]
            
            local.append(sum)
        
        box.append(local)
        
    return box