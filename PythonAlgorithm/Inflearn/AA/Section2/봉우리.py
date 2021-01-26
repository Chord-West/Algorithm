#import sys
#sys.stdin = open("input.txt","rt")


if __name__ == "__main__":
    n=int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    #  R,L,D,U
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    ans=0
    for i in range(n):
        for j in range(n):
            check=True
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if nx<0 or ny<0 or nx>n-1 or ny >n-1:
                    continue
                if board[i][j] <= board[ny][nx]:
                    check=False
                    break

            if check==True:
                ans+=1

    print(ans)