from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        x = q.popleft()
        cnt = 0
        for y in q:
            if x <= y:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer