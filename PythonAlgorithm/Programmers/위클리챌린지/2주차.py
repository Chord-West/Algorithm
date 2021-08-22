from collections import defaultdict
def solution(scores):
    answer = ''
    # 유일한 최고점 , 최저점이면 제외
    for idx,score in enumerate(zip(*scores)):
        p = defaultdict(int)
        for s in score:
            p[s]+=1
        me = score[idx]
        n = len(score)
        sum_score = sum(score)
        if me == max(score) or me == min(score):
            if p[me]==1:
                sum_score-=me
                n-=1
        sum_score/=n
        if sum_score>=90:
            answer+='A'
        elif sum_score>=80:
            answer+='B'
        elif sum_score>=70:
            answer+='C'
        elif sum_score>=50:
            answer+='D'
        else:
            answer+='F'
    return answer