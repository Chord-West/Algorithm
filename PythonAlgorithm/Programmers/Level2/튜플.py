import re
from collections import defaultdict
def solution(s):
    p = defaultdict(int)
    for x in list(map(int,re.sub('[^0-9,]','',s).split(','))):
        p[x]+=1
    return sorted(p,key = lambda x:p[x], reverse = True)