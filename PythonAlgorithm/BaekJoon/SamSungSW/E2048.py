import sys
import copy
sys.stdin = open("input.txt","rt")


def dfs(L,D,c_board):
    r_board = move(D,copy.deepcopy(c_board))
    global ans
    if L == 5:
        for r in r_board:
            ans = max(ans,max(r))
        return
    else:
        dfs(L + 1, 'L',copy.deepcopy(r_board))
        dfs(L + 1, 'R',copy.deepcopy(r_board))
        dfs(L + 1, 'U',copy.deepcopy(r_board))
        dfs(L + 1, 'D',copy.deepcopy(r_board))
        return
def move(D,c_board):
    if D == 'L':
        for i in range(N):
            p=0
            x=0
            for j in range(N):
                if c_board[i][j] == 0:
                    continue
                if x == 0:
                    x = c_board[i][j]
                else:
                    if x == c_board[i][j]:
                        c_board[i][p] = 2*x
                        p = p+1
                        x=0
                    else:
                        c_board[i][p]=x
                        p = p+1
                        x = c_board[i][j]
                c_board[i][j]=0
            if x!=0:
                c_board[i][p]=x
    elif D == 'R':
        for i in range(N):
            p=N-1
            x=0
            for j in range(N-1,-1,-1):
                if c_board[i][j] == 0:
                    continue
                if x == 0:
                    x = c_board[i][j]
                else:
                    if x == c_board[i][j]:
                        c_board[i][p] = 2*x
                        p = p-1
                        x=0
                    else:
                        c_board[i][p]=x
                        p = p-1
                        x = c_board[i][j]
                c_board[i][j]=0
            if x!=0:
                c_board[i][p]=x
    elif D == 'U':
        for i in range(N):
            p = 0
            x = 0
            for q in range(N):
                if c_board[q][i] == 0: continue  # 값이 0 이라면 건너뛴다
                if x == 0:  # 기존에 담고있던 값이 없다면
                    x = c_board[q][i]  # x에 값을 할당
                else:  # 기존에 담고있는 값이 있다면
                    if x == c_board[q][i]:  # 동일한 값이라면
                        c_board[p][i] = 2 * x  # i번째 자리에 2x를 업데이트
                        p = p + 1  # p 한칸 이동
                        x = 0  # x 초기화
                    else:  # 다른 값이라면
                        c_board[p][i] = x  # i번째 자리에 x값 입력
                        p = p + 1  # p 한칸 이동
                        x = c_board[q][i]  # 새로운 x값
                c_board[q][i] = 0  # 나중에 번거로운 작업을 없애주기 위한것
            if x != 0:
                c_board[p][i] = x  # 마지막으로 고려해줘야 할것
    elif D == 'D':
        for i in range(N):
            p = N - 1
            x = 0
            for q in range(N - 1, -1, -1):
                if c_board[q][i] == 0: continue  # 값이 0 이라면 건너뛴다
                if x == 0:  # 기존에 담고있던 값이 없다면
                    x = c_board[q][i]  # x에 값을 할당
                else:  # 기존에 담고있는 값이 있다면
                    if x == c_board[q][i]:  # 동일한 값이라면
                        c_board[p][i] = 2 * x  # i번째 자리에 2x를 업데이트
                        p = p - 1  # p 한칸 이동
                        x = 0  # x 초기화
                    else:  # 다른 값이라면
                        c_board[p][i] = x  # i번째 자리에 x값 입력
                        p = p - 1  # p 한칸 이동
                        x = c_board[q][i]  # 새로운 x값
                c_board[q][i] = 0  # 나중에 번거로운 작업을 없애주기 위한것
            if x != 0: c_board[p][i] = x  # 마지막으로 고려해줘야 할것
    return c_board
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans=0
dfs(0,'',board)
print(ans)