def solution(code):
    a = [code[i:i+8] for i in range(0, len(code), 8)]
    return "".join([chr(int(e, 2)) for e in a])