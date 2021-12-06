def solution(s1, s2):
    d = dict.fromkeys(set(s1), 0)
    for k in d:
        d[k] = min(s1.count(k), s2.count(k))
    return sum(d[k] for k in d)