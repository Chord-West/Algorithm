from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque(map(list, zip(progresses, speeds)))
    cnt = 0
    while q:
        for i in range(len(q)):
            q[i][0] += q[i][1]
        while q and q[0][0] >= 100:
            q.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
            cnt = 0

    return answer