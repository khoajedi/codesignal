def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    strong = max(yourLeft, yourRight) == max(friendsLeft, friendsRight)
    weak = min(yourLeft, yourRight) == min(friendsLeft, friendsRight)
    return strong and weak