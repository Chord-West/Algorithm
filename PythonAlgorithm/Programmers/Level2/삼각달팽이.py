def solution(n):
    answer = []
    maps = [[0] * n for _ in range(n)]
    y, x = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1
            maps[y][x] = num
            num += 1

    for m in maps:
        for x in m:
            if x != 0:
                answer.append(x)
    return answer