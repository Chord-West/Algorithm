# 내 풀이 Runtime : 72ms , Memory
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(x)
            elif x == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(x)
            elif x == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        return True if len(stack) == 0 else False

# 해시 사용 Runtime : 26ms
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0
