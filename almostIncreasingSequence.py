def solution(sequence):
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1]:
            s1 = sequence[:i] + sequence[i+1:]
            s2 = sequence[:i-1] + sequence[i:]
            if len(s1) > len(set(s1)) and len(s2) > len(set(s2)):
                return False
            if s1 != sorted(s1) and s2 != sorted(s2):
                return False
    return True