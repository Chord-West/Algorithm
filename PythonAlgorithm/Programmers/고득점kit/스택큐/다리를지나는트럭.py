from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    q = deque([])
    while True:
        answer += 1
        for i in range(len(q)):
            q[i][1] += 1  # 시간추가
        if len(q) > 0 and q[0][1] > bridge_length:
            q.popleft()
        if len(truck) > 0 and sum(w for w, time in q) + truck[0] <= weight:
            q.append([truck.popleft(), 1])
        if len(q) == 0:
            break

    return answer