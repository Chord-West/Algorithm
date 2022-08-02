import re
from collections import defaultdict
import math

def solution(str1, str2):
    answer = 0
    word_list1=defaultdict(int)
    word_list2=defaultdict(int)
    words = set()
    for i in range(len(str1)-1):
        word1 = re.sub('[^a-z]','',str1[i:i+2].lower())
        if len(word1)>1:
            word_list1[word1]+=1
            words.add(word1)
    for i in range(len(str2)-1):
        word2 = re.sub('[^a-z]','',str2[i:i+2].lower())
        if len(word2)>1:
            word_list2[word2]+=1
            words.add(word2)
    AnB,AuB = 0,0
    for w in words:
        AnB += min(word_list1[w],word_list2[w])
        AuB += max(word_list1[w],word_list2[w])
    if AuB == 0:
        return 65536
    elif AnB == 0:
        return 0
    else:
        return math.trunc(AnB/AuB*65536)
