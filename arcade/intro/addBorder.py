def solution(picture):
    edge = (len(picture[0]) + 2) * "*"
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    return [edge] + picture + [edge]