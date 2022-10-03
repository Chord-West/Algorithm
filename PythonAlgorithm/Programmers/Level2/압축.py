from collections import deque
def solution(msg):
    answer = []
    idx = 27
    p={chr(64+i):i for i in range(1,idx)}
    q = deque([])
    for m in msg:
        q.append(m)
        while q:
            word = ''.join(q)
            if word in p:
                break
            else:
                answer.append(p[word[:-1]])
                p[word] = idx
                idx+=1
                while len(q) > 1:
                    q.popleft()
    answer.append(p[''.join(q)])
    return answer