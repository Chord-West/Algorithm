def solution(arr):
    answer = [arr[0]]
    for x in arr:
        if answer[-1]==x:
            continue
        else:
            answer.append(x)
    return answer