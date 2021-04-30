import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline
sys.setrecursionlimit(10000)
n,r,c = map(int,r().split())
print(n,r,c)
Z = [[0]*pow(2,n) for _ in range(pow(2,n))]
count=0
 # N =4->2->1
def zigzag(x,y,N):
    global count
    if N==2:
        if x == c and y == r:
            print(count)
            return
        count+=1
        if x+1 == c  and y == r:
            print(count)
            return
        count+=1
        if x == c and y+1 == r:
            print(count)
            return
        count+=1
        if x+1 == c and y+1 == r:
            print(count)
            return
        count+=1
    else:
        zigzag(x,y,N//2)
        zigzag(x+N//2, y, N // 2)
        zigzag(x , y + N // 2, N // 2)
        zigzag(x + N // 2, y + N // 2 , N // 2)

zigzag(0,0,pow(2,n))

