def solution(answers):
    answer = []
    su1 = [1,2,3,4,5]*2000
    su2 = [2,1,2,3,2,4,2,5]*2000
    su3 = [3,3,1,1,2,2,4,4,5,5]*2000
    tmp = [0,0,0]
    for i in range(len(answers)):
        if answers[i] ==su1[i]:
            tmp[0]+=1
        if answers[i] ==su2[i]:
            tmp[1]+=1
        if answers[i] ==su3[i]:
            tmp[2]+=1
    tmp_max = max(tmp)
    for idx,t in enumerate(tmp):
        if t == tmp_max:
            answer.append(idx+1)
    return answer