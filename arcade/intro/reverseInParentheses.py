def solution(inputString):
    while '(' in inputString:
        l = inputString.rfind('(')
        r = inputString.find(')',l+1)
        s1 = inputString[:l]
        s2 = inputString[l+1:r][::-1]
        s3 = inputString[r+1:]
        inputString = s1 + s2 + s3
    return inputString