def solution(arr):
    answer = arr
    arr.pop(arr.index(min(arr)))
    if len(answer)==0:
        answer.append(-1)
    return answer