def solution(s):
    answer = True
    p = dict()
    for x in s.lower():
        if x=='p' or x =='y':
            p[x]=p.get(x,0)+1
    if len(p)==0:
        return True
    if p.get('p',-1)!=p.get('y',-2):
        answer=False
    return answer