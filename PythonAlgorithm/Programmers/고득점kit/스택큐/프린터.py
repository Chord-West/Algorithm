from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(v, idx) for idx, v in enumerate(priorities)])
    stack = []
    tmp = []
    while q:
        paper = q.popleft()
        while len(stack) > 0 and stack[-1][0] < paper[0]:
            tmp.append(stack.pop())
        while tmp:
            q.append(tmp.pop())
        stack.append(paper)
    for idx, v in enumerate(stack):
        if v[1] == location:
            answer = idx + 1

    return answer