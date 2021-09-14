from collections import defaultdict
from heapq import heappush,heappop

def solution(table, languages, preference):
    answer = ''
    p = defaultdict(dict)
    lang = ['SI','CONTENTS','HARDWARE','PORTAL','GAME']
    lang_p = defaultdict(int )
    heap=[]
    for t in table:
        tmp = t.split(' ')
        for idx,v in enumerate(tmp[1:][::-1]):
            p[tmp[0]][v]=idx+1
    for l in lang:
        for i in range(len(languages)):
            if languages[i] in p[l]:
                lang_p[l]+=p[l][languages[i]]*preference[i]
    for k,v in lang_p.items():
        heappush(heap,(-v,k))
    answer = heappop(heap)[1]
    return answer