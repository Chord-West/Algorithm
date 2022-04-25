# 159 ms	17.2 MB

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = defaultdict(list)
        result = []
        for word in strs:
            s = ''.join(sorted(list(map(str,word))))
            p[s].append(word) 
        for k,v in p.items():
            result.append(v)
        return result