from itertools import permutations

def solution(inputArray):
    perms = permutations(inputArray)
    
    for p in perms:
        flag = True
        
        for a, b in zip(p[1:], p[:-1]):
            diff = sum(1 if a[i] != b[i] else 0 for i in range(len(a)))
            if diff != 1:
                flag = False
                break
        
        if flag:
            return True
        
    return False