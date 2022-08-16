from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([[n,idx] for idx,n in enumerate(priorities)])
    stack = []
    while q:
        prt = q.popleft()
        t_stack = []
        while stack and stack[-1][0] < prt[0]:
            t_stack.append(stack.pop())
        else:
            stack.append(prt)
        while t_stack:
            q.append(t_stack.pop())
    for idx,v in enumerate(stack):
        if location == v[1]:
            answer = idx+1
    return answer