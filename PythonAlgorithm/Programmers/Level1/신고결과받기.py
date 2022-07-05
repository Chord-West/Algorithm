from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    p = defaultdict(set)
    result = {x: 0 for x in id_list}
    for x in report:
        a, b = x.split()
        p[b].add(a)
    for id in id_list:
        if len(p[id]) >= k:
            for x in p[id]:
                result[x] += 1

    return list(result.values())