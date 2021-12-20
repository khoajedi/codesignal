def solution(n):
    a = []
    
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        a.append(temp)
    
    c = 1
    d = 'right'
    i = j = 0
    
    while c < n * n:
        while d == 'right':
            a[i][j] = c
            c += 1
            j += 1
            if j == n or a[i][j] > 0:
                j -= 1
                c -= 1
                d = 'down'
            if c > n * n:
                return a
            
        while d == 'down':
            a[i][j] = c
            c += 1
            i += 1
            if i == n or a[i][j] > 0:
                i -= 1
                c -= 1
                d = 'left'
            if c > n * n:
                return a
             
        while d == 'left':
            a[i][j] = c
            c += 1
            j -= 1
            if j < 0 or a[i][j] > 0:
                j += 1
                c -= 1
                d = 'up'
            if c > n * n:
                return a
            
        while d == 'up':
            a[i][j] = c
            c += 1
            i -= 1
            if i < 0 or a[i][j] > 0:
                i += 1
                c -= 1
                d = 'right'
            if c > n * n:
                return a
                
    return a