from heapq import heappush,heappop

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # h = 키, k = 앞에 줄 서 있는 자신의 키 이상
        heap=[]
        for person in people:
            heappush(heap,(-person[0],person[1]))
        result=[]
        while heap:
            person = heappop(heap)
            result.insert(person[1],[-person[0],person[1]])

        return result