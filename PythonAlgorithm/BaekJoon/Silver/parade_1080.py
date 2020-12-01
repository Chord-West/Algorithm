import sys

sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
a=[list(map(int,list(input()))) for _ in range(n)]
b=[list(map(int,list(input()))) for _ in range(n)]



cnt =0

def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j]=1-a[i][j]

def checkEquality():
    for i in range(n):
        for j in range(m):
            if a[i][j] !=b[i][j]:
                return 0
    return 1

for i in range(0,n-2):
    for j in range(0,m-2):
        if a[i][j]!=b[i][j]:
            reverse(i,j)
            cnt+=1

if checkEquality():
    print(cnt)
else:
    print(-1)
    

