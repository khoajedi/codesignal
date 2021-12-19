def solution(n):
    s = str(n)
    a = []
    
    for i in range(len(s)):
        a.append(int(s[:i] + s[i+1:]))

    return max(a)