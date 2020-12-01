import sys
sys.stdin = open("input.txt","rt")

def dfs(start,net,visited):
    visited[start]=True
    global count
    count+=1
    for x in net[start]:
        if not visited[x]:
            dfs(x,net,visited)
    return count

n = int(input()) # 컴퓨터 개수
m = int(input()) # 컴퓨터 쌍 

net =[[] for _ in range(n+1)] # 초기화

visited=[False]*(n+1) # visietd 초기화

for _ in range(m):
    x ,y = map(int,input().split())
    net[x].append(y)
    net[y].append(x)

for x in net:
    x.sort()

count =0 
print(dfs(1,net,visited)-1)
