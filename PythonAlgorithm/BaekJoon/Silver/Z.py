import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline

n,r,c = map(int,r().split())
print(n,r,c)
Z = [[0]*pow(2,n) for _ in range(pow(2,n))]

 # N =4->2->1
def zigzag(x,y,N):

    if N==1:
    else:
        zigzag(x,y,N//2)
        zigzag(x+N//2, y, N // 2)
        zigzag(x,y+N//2,N//2)
        zigzag(x+N//2,y+N//2,N//2)

