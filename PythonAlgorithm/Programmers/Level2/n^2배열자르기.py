def solution(n, left, right):
    answer = []
    lx, ly = left % n, left // n
    rx, ry = right % n, right // n
    for i in range(ly, ry + 1):
        for _ in range(i + 1):
            answer.append(i + 1)
        for j in range(n - i - 1):
            answer.append(i + j + 2)

    idx = n - rx - 1
    if idx == 0:
        answer = answer[lx:]
    else:
        answer = answer[lx:-idx]

    return answer