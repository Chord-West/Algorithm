from collections import deque
import sys

sys.stdin = open("input.txt","rt")

n, m = map(int,input().split())

frame = [list(map(int,input())) for _ in range(n)]

count = 0

def dfs(x,y):
    if x< 0 or x>n-1 or y <0 or y > m-1:
        return False
    if frame[x][y] == 0:
        frame[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1
                    
            
print(count)