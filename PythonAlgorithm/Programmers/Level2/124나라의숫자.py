from collections import deque
def solution(n):
    answer = ''
    stack =[]
    while n>0:
        if n%3==0:
            n-=1
            stack.append('4')
        else:
            stack.append(str(n%3))
        n=n//3
    while stack:
        answer+=stack.pop()
    return answer

print(solution(6))