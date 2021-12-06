def solution(inputString):
    s = set(inputString)
    flag = False
    for x in s:
        c = inputString.count(x)
        if c % 2 == 1:
            if flag:
                return False
            flag = True
    return True