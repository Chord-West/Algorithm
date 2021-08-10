from heapq import heappop,heappush,heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        x = heappop(scoville)
        if x >=K:
            break
        if not scoville:
            return -1
        y = heappop(scoville)
        heappush(scoville,x+y*2)
        answer+=1
    return answer