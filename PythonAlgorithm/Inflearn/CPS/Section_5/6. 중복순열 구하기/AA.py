##강의 풀이

import sys
#sys.stdin = open("input.txt","rt")

def DFS(idx):
    global cnt
    if idx==m:
        for j in range(m):
            print(arr[j],end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            arr[idx]=i
            DFS(idx+1)

if __name__=="__main__":
    n,m = map(int,input().split())
    arr=[0]*n
    cnt=0
    DFS(0)
    print(cnt)