from heapq import heappush, heappop


def solution(jobs):
    answer, start, now = 0, -1, 0
    size = len(jobs)
    heap = []
    cnt = 0
    while cnt < size:
        for job in jobs:
            if start < job[0] <= now:
                heappush(heap, (job[1], job[0]))
        if heap:
            current = heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            cnt += 1
        else:
            now += 1

    return answer // size