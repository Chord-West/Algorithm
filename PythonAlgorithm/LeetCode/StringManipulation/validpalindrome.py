# 첫 풀이 90 ms	14.3 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        word = ''
        for x in s:
            if x.isalnum():
                word+=x
        idx=0
        while idx < len(word):
            if word[idx] != word[-1-idx]:
                return False
            idx+=1
        return True

# 두번쨰 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for x in s.lower():
            if x.isalnum():
                word+=x            
        return word==word[::-1]
    
# 정규표현식 이용
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        word = re.sub('[^a-z0-9]', '', word)
        return word == word[::-1]


