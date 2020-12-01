import sys
sys.stdin = open("input.txt","rt")

n = int(input()) # 가족수
x,y = map(int,input().split()) # x 부모 ,y 자식
m = int(input()) # 관계수

tree = [[] for _ in range(n+1)]

def dfs(tree,v,count):
    visited[v]=count

    for i in tree[v]:
        if visited[i]==0:
            dfs(tree,i,count+1)
            
   

for _ in range(m):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

for k in tree:
    k.sort()


visited = [0]*(n+1) 
count=1

dfs(tree,y,count)
print(visited[x]-1)
