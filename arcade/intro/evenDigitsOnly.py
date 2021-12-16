def solution(n):
    for c in str(n):
        if int(c) % 2 != 0:
            return False
    
    return True

def solutionV2(n):
    return all([int(x) % 2 == 0 for x in str(n)])