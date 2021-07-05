class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=''
        for char in s:
            if char.isalnum():
                word+=char.lower()
        return word==word[::-1]

# 정규표현식 이용
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        word = re.sub('[^a-z0-9]', '', word)
        return word == word[::-1]


