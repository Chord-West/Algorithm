def solution(places):
    answer = []
    # 대기실은 5개, 5x5  , |r1 - r2| + |c1 - c2| 2이하 불가능
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    def dfs(x,y):
        nonlocal ch
        if maps[y][x]=='P':
            if abs(gx-x) + abs(gy-y) <=2:
                ch=False
        if abs(gx-x) + abs(gy-y) >2:
            return
        else:
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and chmap[ny][nx]==0 and (maps[ny][nx]=='O' or maps[ny][nx]=='P'):
                    chmap[ny][nx]=1
                    dfs(nx,ny)

    for place in places:
        maps= [list(p) for p in place]
        p_locations=[]
        for y,p in enumerate(place):
            for x,v in enumerate(p):
                if v =='P':
                    p_locations.append([x,y])
        ch=True
        for x,y in p_locations:
            chmap = [[0]*5 for _ in range(5)]
            gx,gy=x,y
            chmap[gy][gx]=1
            maps[gy][gx]='O'
            dfs(x,y)
            if not ch:
                break
        if ch:
            answer.append(1)
        else:
            answer.append(0)

    return answer