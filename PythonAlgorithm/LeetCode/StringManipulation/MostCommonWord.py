import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z0-9]',' ',paragraph.lower()).split()
        p = dict()
        for word in paragraph:
            p[word] = p.get(word,0)+1
        print(p)
        tmp_max=0
        answer=''
        for k,v in p.items():
            if tmp_max<v and k not in banned:
                tmp_max=v
                answer=k
        return answer

# Couter , 사용

import re
from collections import defaultdict,Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph.lower()).split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]