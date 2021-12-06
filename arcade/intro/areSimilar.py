def solution(a, b):
    a1 = []
    b1 = []
    for i in range(len(a)):
        if a[i] != b[i]:
            a1.append(a[i])
            b1.append(b[i])
    if len(a1) == 0:
        return True
    if len(a1) != 2:
        return False
    return a1 == b1[::-1]