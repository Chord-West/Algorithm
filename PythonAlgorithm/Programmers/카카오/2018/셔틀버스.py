from collections import deque


def solution(n, t, m, timetable):
    answer = ''
    # ??? 9? ?? n? t? ?? , m : ?? ?? ? # timetable ??? ??? ??
    bustime = deque([9 * 60 + i * t for i in range(n)])
    check = [[] for _ in range(n)]
    crew = []
    for time in timetable:
        h, mi = time.split(':')
        t = int(h) * 60 + int(mi)
        crew.append(t)
    crew.sort()
    crew = deque(crew)
    idx = 0
    while bustime:
        cur_time = bustime.popleft()  # ????
        while crew and crew[0] <= cur_time:
            check[idx].append(crew.popleft())
            if len(check[idx]) == m:  # ???? ?? ??
                break
        idx += 1
        if idx > n - 1:
            break
    if len(check[-1]) == m:
        tmp = check[-1][-1] - 1
        h = tmp // 60
        m = tmp % 60
    else:
        h = cur_time // 60
        m = cur_time % 60
    answer = '{0:02d}:{1:02d}'.format(h, m)
    return answer