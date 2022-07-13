from collections import deque
def solution(board, moves):
    answer = 0
    crain = [deque([x for x in row if x!=0]) for row in zip(*board)]
    stack=[]
    for move in moves:
        if crain[move-1]:
            doll = crain[move-1].popleft()
            if stack and stack[-1]==doll:
                stack.pop()
                answer+=2
            else:
                stack.append(doll)
    return answer