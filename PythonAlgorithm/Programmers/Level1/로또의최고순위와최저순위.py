
def solution(lottos, win_nums):
    answer = []
    anssum = 0
    zerosum = 0
    p = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    for x in lottos:
        if x in win_nums:
            anssum +=1
        elif x == 0:
            zerosum += 1
    print(anssum,zerosum)
    answer = [p[anssum+zerosum],p[anssum]]
    return answer