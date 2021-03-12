from collections import deque

def solution(s):
    q = deque(s)
    stack=[q.popleft()]
    while q:
        x = q.popleft()
        if len(stack)>0 and stack[-1]==x:
            stack.pop()
        else:
            stack.append(x)
    if len(stack)==0:
        return 1
    else:
        return 0