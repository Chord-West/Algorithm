class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = dict()
        p = {')': '(', '}': '{', ']': '['}

        for x in s:
            if x not in p:
                stack.append(x)
            elif not stack or p[x] != stack.pop():
                return False
        return len(stack) == 0
