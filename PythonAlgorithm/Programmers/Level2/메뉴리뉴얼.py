from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        p = defaultdict(int)
        for order in orders:
            for x in combinations(order,c):
                p[''.join(sorted(x))]+=1
        if p:
            size = max(p.values(),key= lambda x:x)
            for k,v in p.items():
                if size ==v and size>1:
                    answer.append(k)
    answer.sort()
    return answer