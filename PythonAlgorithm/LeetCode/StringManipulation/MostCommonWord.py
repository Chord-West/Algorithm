# 54 ms	14 MB
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = dict()
        words = re.sub('[^a-z]',' ',paragraph.lower())
        for word in words.split():
            if word not in banned:
                p[word]=p.get(word,0)+1
        p = sorted(p.items(), key = lambda x:x[1], reverse = True)
        return p[0][0]
    

# Couter , 사용    50 ms	14 MB

import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = dict()
        words = [word for word in re.sub('[^a-z]',' ',paragraph.lower()).split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]
       