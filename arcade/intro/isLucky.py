def solution(n):
    s = str(n)
    m = len(s) // 2
    return sum(int(x) for x in s[:m]) == sum(int(x) for x in s[m:])