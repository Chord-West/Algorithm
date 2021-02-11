def solution(strings, n):
    answer=sorted(strings,key= lambda x:x[n])
    answer.sort()
    return answer