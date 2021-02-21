def solution(progresses, speeds):
    answer = []
    size = len(progresses)
    while progresses:
        tmp = 0
        for i in range(size):
            progresses[i] += speeds[i]
        while progresses and progresses[0] > 99:
            progresses.pop(0)
            speeds.pop(0)
            tmp += 1
        if tmp > 0:
            size -= tmp
            answer.append(tmp)

    return answer