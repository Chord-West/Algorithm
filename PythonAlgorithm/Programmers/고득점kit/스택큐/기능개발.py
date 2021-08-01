from collections import deque

def solution(progresses, speeds):
    answer=[]
    q = deque(progresses)
    speeds = deque(speeds)
    n = len(speeds)
    while q:
        for i in range(n):
            q[i]+=speeds[i]
        if q[0] >=100:
            cnt=0
            while len(q)>0 and q[0]>=100:
                q.popleft()
                speeds.popleft()
                cnt+=1
                n-=1
            answer.append(cnt)
    return answer