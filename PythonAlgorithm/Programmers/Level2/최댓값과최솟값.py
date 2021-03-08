def solution(s):
    answer = ''
    li = list(map(int,s.split()))
    answer= str(min(li))+" "+str(max(li))
    return answer