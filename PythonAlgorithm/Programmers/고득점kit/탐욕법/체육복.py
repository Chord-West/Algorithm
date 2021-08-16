def solution(n, lost, reserve):
    answer = 0
    people = [1] * n
    dx = [-1, 1]
    for r in reserve:
        people[r - 1] += 1
    for l in lost:
        people[l - 1] -= 1
    for i in range(n):
        if people[i] == 2:
            for x in dx:
                nx = i + x
                if 0 <= nx < n and people[nx] == 0 and people[i] == 2:
                    people[nx] += 1
                    people[i] -= 1
    for p in people:
        if p > 0:
            answer += 1

    return answer