from collections import deque

def solution(s):
    answer = 0
    q = deque(list(map(str, s)))
    for _ in range(len(s)):
        answer += validate(q)
        q.append(q.popleft())
    return answer

def validate(q):
    stack = []
    br = list(q)
    while br:
        x = br.pop(0)
        if x == ']':
            if stack and stack[-1] == '[': stack.pop()
            else: stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(': stack.pop()
            else: stack.append(x)
        elif x == '}':
            if stack and stack[-1] == '{': stack.pop()
            else: stack.append(x)
        else:
            stack.append(x)
    if len(stack) == 0:
        return 1
    else:
        return 0


