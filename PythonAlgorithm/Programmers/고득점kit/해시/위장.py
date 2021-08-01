from collections import defaultdict
def solution(clothes):
    answer=1
    p = defaultdict(list)
    for item,category in clothes:
        p[category].append(item)
    for v in p.values():
        answer*=(len(v) +1)

    return answer-1