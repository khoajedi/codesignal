def solution(inputString):
    a = re.findall("(\d*)", inputString)
    return sum(int(e) for e in a if e.isdigit())