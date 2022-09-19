from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque([],maxlen=cacheSize)
    for city in cities:
        x = city.lower()
        if x in q:
            q.remove(x)
            answer+=1
        else:
            answer+=5
        q.append(x)
    return answer