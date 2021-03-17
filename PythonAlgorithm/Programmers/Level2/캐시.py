from collections import deque


def solution(cacheSize, cities):
    answer = 0
    q = deque(maxlen=cacheSize)
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        c = city.lower()
        if c in q:
            answer += 1
            q.remove(c)
            q.append(c)
        else:
            answer += 5
            q.append(c)

    return answer