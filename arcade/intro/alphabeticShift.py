def solution(inputString):
    return "".join([chr(ord(c) + 1) if c != "z" else "a" for c in inputString])