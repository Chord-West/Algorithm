from collections import deque


def solution(priorities, location):
    answer = []
    num = [x for x in range(0, len(priorities))]
    Q = deque(zip(priorities, num))
    while Q:
        x, y = Q.popleft()  # 2,0
        for xq, yq in Q:
            if x < xq:
                Q.append((x, y))
                break
        else:
            answer.append(y)

    return answer.index(location) + 1