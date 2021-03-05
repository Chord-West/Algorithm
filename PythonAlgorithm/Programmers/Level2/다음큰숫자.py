def solution(n):
    onenum = sum(1 for x in bin(n)[2:] if x == '1')
    for x in range(n + 1, 1000001):
        if onenum == sum(1 for y in bin(x)[2:] if y == '1'):
            return x
