def solution(a):
    z = [x for x in a if x > 0]
    z = sorted(z)
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = z.pop(0)
    return a