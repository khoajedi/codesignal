def solution(m):
    w = len(m[0])
    h = len(m)
    a = []
    
    for i in range(h - 1):
        for j in range(w - 1):
            s = str(m[i][j]) + str(m[i][j+1]) + str(m[i+1][j]) + str(m[i+1][j+1])
            a.append(s)
            
    return len(set(a))

def solutionV2(m):
    s = set()
    
    for i in range(len(m) - 1):
        for j in range(len(m[0]) - 1):
            s.add((m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1]))
            
    return len(s)