def solution(numbers, hand):
    answer = ''
    keypad = {
        1:[0,0],2:[0,1],3:[0,2]
        ,4:[1,0],5:[1,1],6:[1,2]
        ,7:[2,0],8:[2,1],9:[2,2]
        ,0:[3,1]
    }
    ly,lx = 3,0
    ry,rx = 3,2
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            ly,lx = keypad[n]
            answer+='L'
        elif n == 3 or n == 6 or n == 9:
            ry,rx = keypad[n]
            answer+='R'
        else:
            dy,dx = keypad[n]
            LD = abs(ly-dy) + abs(lx-dx)
            RD = abs(ry-dy) + abs(rx-dx)
            if LD < RD :
                ly,lx = dy,dx
                answer+='L'
            elif LD > RD:
                ry,rx = dy,dx
                answer+='R'
            else:
                if hand=='right':
                    ry,rx = dy,dx
                    answer+='R'
                else:
                    ly,lx = dy,dx
                    answer+='L'
    return answer