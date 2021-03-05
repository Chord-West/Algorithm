from collections import deque

def solution(s):
    stack=[]
    q=deque(x for x in s)
    if q[0]==')':
        return False
    else:
        stack.append(q.popleft())
    while q:
        x = q.popleft()
        if x=='(':
            stack.append(x)
        else: # )일때
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
    if len(stack)==0:
        return True
    else:
        return False