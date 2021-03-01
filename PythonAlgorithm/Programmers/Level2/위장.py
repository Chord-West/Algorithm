def solution(clothes):
    answer = 1
    p = dict()
    for v,k in clothes:
        p[k] = p.get(k,0)+1
    for x in p.values():
        answer*=(x+1)
    return answer-1