def solution(n):
    return sum(int(x) for x in str(n // 60)) + sum(int(x) for x in str(n % 60))