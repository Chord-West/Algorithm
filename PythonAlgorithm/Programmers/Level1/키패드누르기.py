def solution(numbers, hand):
    answer = ''
    pad=[[1,4,7,-1],[2,5,8,0],[3,6,9,-2]]
    lx,ly,rx,ry=3,3,3,3
    for n in numbers:
        for idx,p in enumerate(pad):
            if n in p:
                if idx==0: # L
                    answer+='L'
                    lx,ly=idx,n
                if idx==1: # M
                    if abs((lx-idx)+(ly-n)) < abs((rx-idx)+(ry-n)):
                        answer+='L'
                        lx,ly=idx,n
                    elif abs((lx-idx)+(ly-n)) > abs((rx-idx)+(ry-n)):
                        answer+='R'
                        rx,ry=idx,n
                    else:
                        if hand=='right':
                            answer+='R'
                            rx,ry=idx,n
                        else:
                            answer+='L'
                            lx,ly=idx,n
                if idx==2: # R
                    answer+='R'
                    rx,ry=idx,n
    return answer

a=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
b='right'
print(solution(a,b))