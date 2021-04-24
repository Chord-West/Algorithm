def solution(dirs):
    answer = 0
    maps = [[0]*21 for _ in range(21)]
    sx,sy = 10,10
    for x in dirs:
        if x == 'U':
            if sy-2>=0:
                if maps[sy-1][sx]==0:
                    maps[sy-1][sx]=1
                    answer+=1
                sy-=2
        elif x == 'D':
            if sy+2<21:
                if maps[sy+1][sx]==0:
                    maps[sy+1][sx]=1
                    answer+=1
                sy+=2
        elif x == 'L' :
            if sx-2>=0:
                if maps[sy][sx-1]==0:
                    maps[sy][sx-1]=1
                    answer+=1
                sx-=2

        elif x == 'R' :
            if sx+2<21:
                if maps[sy][sx+1]==0:
                    maps[sy][sx+1]=1
                    answer+=1
                sx+=2

    return answer