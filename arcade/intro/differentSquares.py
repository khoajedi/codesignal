def solution(m):
    w = len(m[0])
    h = len(m)
    a = []
    
    for i in range(h - 1):
        for j in range(w - 1):
            s = str(m[i][j]) + str(m[i][j+1]) + str(m[i+1][j]) + str(m[i+1][j+1])
            a.append(s)
            
    return len(set(a))