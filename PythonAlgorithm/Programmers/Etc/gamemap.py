from collections import deque

def solution(maps):
    answer = -1
    xlim,ylim=len(maps[0])-1,len(maps)-1 # 맵의 범위

    #   R,L,D,U
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    def bfs(y,x):
        queue=deque()
        queue.append((y,x))
        nonlocal answer
        while queue:
            y,x = queue.popleft()
            for i in range(4):
                ny=y+dy[i]
                nx=x+dx[i]

                if nx<0 or nx>xlim or ny<0 or ny>ylim:
                    continue
                if maps[ny][nx] == 0:
                    continue
                if maps[ny][nx]==1:
                    maps[ny][nx]=maps[y][x]+1

                    queue.append((ny,nx))
            answer= maps[ylim][xlim]

    bfs(0,0)
    return answer

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))