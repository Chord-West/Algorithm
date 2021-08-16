def solution(name):
    answer = 0
    n = len(name)
    updown = [min(ord(n)-65,91-ord(n))for n in name]
    locat = 0
    while 1:
        answer += updown[locat]
        updown[locat] = 0
        if sum(updown) == 0: break
        left = 1
        right = 1
        while updown[locat + right] == 0:
            right += 1
        while updown[locat - left] == 0:
            left += 1
        if left >= right:
            locat += right
            answer += right
        else:
            locat -= left
            answer += left
    return answer