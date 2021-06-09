import sys
sys.stdin = open("input.txt","rt")
def divide(x,y,end):
    global ans

    start = tree[y][x]
    for i in range(y,y+end):
        for j in range(x,x+end):
            if start != tree[i][j]:
                end = end // 2
                ans+='('
                divide(x,y,end)
                divide(x+end, y, end)
                divide(x, y+end, end)
                divide(x + end, y+end, end)
                ans += ')'
                return
    else:
        ans+=str(start)

n = int(input())
tree = [[int(i) for i in input()] for _ in range(n)]
ans=''

divide(0,0,n)
print(ans)