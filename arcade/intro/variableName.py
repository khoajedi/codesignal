def solution(name):
    if not name[0].isalpha() and not name[0] == "_":
        return False
    for c in name[1:]:
        if not c.isdigit() and not c.isalpha() and not c == "_":
            return False
    return True