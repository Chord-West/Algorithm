def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget-=i
        answer+=1
        if(budget<0):
            budget+=i
            answer-=1
            continue
    return answer