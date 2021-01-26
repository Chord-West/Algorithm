import sys
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    n,m=map(int,input().split())
    arr=[[0]*n for _ in range(n)]
    for _ in range(m):
        r,c,v = map(int,input().split())
        arr[r-1][c-1]=v
    for x in arr:
        print(" ".join(map(str,x)))
