from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossed = [0] * bridge_length
    q = deque(truck_weights)
    while crossed:
        answer+=1
        crossed.pop(0)
        if q:
            if sum(crossed)+q[0]<=weight:
                crossed.append(q.popleft())
            else:
                crossed.append(0)
    return answer