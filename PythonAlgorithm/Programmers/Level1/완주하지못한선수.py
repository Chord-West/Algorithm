def solution(participant, completion):
    answer = ''
    p = dict()
    for x in participant:
        p[x]=p.get(x,0)+1
    for x in completion:
        p[x]=p.get(x,0)+1
    for k,v in p.items():
        if v%2==1:
            answer=k
    return answer