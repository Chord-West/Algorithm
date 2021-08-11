from heapq import heappop,heappush
def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        oper,num = operation.split()
        num = int(num)
        if oper=='I':
            heappush(max_heap,(-num))
            heappush(min_heap,(num))
        else:
            if min_heap:
                if num==1: # 최댓값 삭제
                    max_value=heappop(max_heap)
                    min_heap.remove(-max_value)
                else:
                    min_value = heappop(min_heap)
                    max_heap.remove(-min_value)
    if min_heap:
        return [-heappop(max_heap), heappop(min_heap)]
    else:
        return [0,0]