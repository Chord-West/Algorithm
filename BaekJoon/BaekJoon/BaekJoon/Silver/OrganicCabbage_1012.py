from collections import deque
import sys

sys.stdin = open("input.txt","rt")


def dfs(x,y):
    if x<0 or x>n-1 or y<0 or y>m-1 :
        return False
    if land[x][y] ==1:
        land[x][y]=2
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x-1,y)
        return True
    return False



t = int(input()) # 테스트 케이스

for _ in range(t):
    m,n,k = map(int,input().split()) # m : 가로, n : 세로,  k : 배추수
    land = [[0]*m  for _ in range(n)] 
    count=0
    for _ in range(k):
        y,x = map(int,input().split()) # x,y 배추위치
        land[x][y] = 1  # 배추 초기화
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                count+=1
    print(count)

