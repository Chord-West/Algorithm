# 내 방법 Runtime : 100ms, Memory : 17.2 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p=dict()
        answer=[]
        for word in strs:
            p[''.join(sorted(word))]=[]
        for word in strs:
             p[''.join(sorted(word))].append(word)
        for k,v in p.items():
            answer.append(v)
        return answer

#정렬하여 딕셔너리에 추가 ( defaultdict 활용 ) : Runtime : 92ms, Memory : 17.1MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p=dict()
        answer=[]
        for word in strs:
            p[''.join(sorted(word))]=[]
        for word in strs:
             p[''.join(sorted(word))].append(word)
        for k,v in p.items():
            answer.append(v)
        return answer