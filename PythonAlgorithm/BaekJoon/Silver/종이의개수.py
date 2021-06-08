import sys
sys.stdin = open("input.txt","rt")

n = int(input())
papers = [ list(map(int,input().split())) for _ in range(n)]
answer=[0,0,0]

def divide(x, y, end):
    start = papers[y][x]
    for i in range(y, end + y):
        for j in range(x, end + x):
            if start != papers[i][j]:
                end=end//3
                for a in range(3):
                    for b in range(3):
                        divide(x+b*end,y+a*end,end)
                return
    else:
        if start==-1:
            answer[0]+=1
        elif start==0:
            answer[1]+=1
        else:
            answer[2]+=1
divide(0,0,n)
for ans in answer:
    print(ans)