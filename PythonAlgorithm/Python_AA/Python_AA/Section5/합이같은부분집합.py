import sys
sys.stdin = open("input.txt","rt")

def DFS(idx,sum):
    if sum>total//2:
        return 
    if idx==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(idx+1,sum+num[idx])
        DFS(idx+1,sum)

if __name__ == "__main__":
    n=int(input())
    num = list(map(int,input().split()))
    total=sum(num)
    DFS(0,0)
    print("NO")