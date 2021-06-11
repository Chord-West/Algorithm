import sys

from collections import deque
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    func = input()
    length = int(input())
    q = deque(input()[1:-2].split(','))

    if length == 0:
        q = deque()

    isError = False
    isReverse = False
    for c in func:
        if c == 'R':
            isReverse = not isReverse
        else:
            if not q:
                isError = True
                break
            if isReverse:
                q.pop()
            else:
                q.popleft()

    if not isError:
        if isReverse:
            q.reverse()
        q = list(q)
        print('[', end='')
        print(','.join(q), end='')
        print(']')
    else:
        print('error')