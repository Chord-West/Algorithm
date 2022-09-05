from itertools import combinations as com
from collections import defaultdict
import re
from bisect import bisect_left


def solution(infos, queries):
    answer = []
    p = defaultdict(list)
    for info in infos:
        li, score = info.split()[:-1], int(info.split()[-1])
        for i in range(5):
            for c in com(li, i):
                p[''.join(c)].append(score)
    for x in p.keys():
        p[x].sort()

    for query in queries:
        q = re.sub('-', '', re.sub('and', '', query)).split()
        target, score2 = ''.join(q[:-1]), int(q[-1])
        if target in p:
            tarlist = p[target]
            index = bisect_left(tarlist, score2)
            answer.append(len(tarlist) - index)
        else:
            answer.append(0)
    return answer