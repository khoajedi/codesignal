def solution(votes, k):
    m = max(votes)
    
    if k == 0 and votes.count(m) == 1:
        return 1
        
    return sum(1 if (v + k) > m else 0 for v in votes)