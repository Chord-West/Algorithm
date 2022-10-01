from collections import defaultdict


def solution(fees, records):
    answer = []
    parking = defaultdict(int)
    # 시간, 기본요금, 시간, 시간당 요금
    for fee in fees:
        print(fee)
    for record in records:
        time, num, info = record.split()
        h, m = map(int, time.split(":"))
        MM = 60 * h + m
        if info == 'IN':
            parking()
        print(MM)

    return answer