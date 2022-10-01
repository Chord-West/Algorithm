from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    park = defaultdict(list)
    last = 60 * 23 + 59
    for record in records:
        time, num, info = record.split()
        h, m = map(int, time.split(":"))
        MM = 60 * h + m
        park[num].append(MM)

    for k, v in park.items():
        if len(v) % 2 == 1:
            park[k].append(last)

    for x in sorted(park):
        t_sum = 0
        for i in range(0, len(park[x]), 2):
            t_sum += park[x][i + 1] - park[x][i]
        if t_sum <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((t_sum - fees[0]) / fees[2]) * fees[3])

    return answer