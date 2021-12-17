def solution(a):
    size = len(a)
    if size % 2 == 0:
        return a[size // 2 - 1]
    return a[size // 2]

def solutionV2(a):
    return a[(len(a) - 1) // 2]