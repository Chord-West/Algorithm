def solution(a, b):
    answer = [x for x in range(min(a,b),max(a,b)+1)]
    return sum(answer)