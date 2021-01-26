from collections import defaultdict,deque

import sys
sys.stdin = open("input.txt","rt")

n = int(input())

signs = [list(map(int,input().split())) for _ in range(3)]



def bfs(start,des,table):
    visited = set() # 중복 피하기
    queue = deque()
    queue.append(start)
    while queue:
        next = queue.popleft()
        visited.add(next)
        for i in table[next]:
            if i ==des:
                return 1
            elif i not in visited:
                queue.append(i)
                visited.add(i)

    return 0


def solution(n,signs):
    table = defaultdict(set)
    for y in range(n):
        for x in range(n):
            if signs[y][x]==1:
                table[y].add(x)
 
    answer=[[0]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            answer[y][x] = bfs(y,x,table) 

    print(answer)



solution(n,signs)