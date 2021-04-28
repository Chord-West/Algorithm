import sys
sys.stdin = open('input.txt','rt')
r = sys.stdin.readline
n = int(r())
board = [ list(map(int,r().split())) for _ in range(n)]
result = []
def check(x,y,n):
    color = board[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if color != board[i][j]:
                check(x, y , n // 2)
                check(x,y+n//2,n//2)
                check(x+n//2,y,n//2)
                check(x+n//2,y+n//2,n//2)
                return

    if color==0:
        result.append(0)
    else:
        result.append(1)
check(0,0,n)

print(result.count(0))
print(result.count(1))

