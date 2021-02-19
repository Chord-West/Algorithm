# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
def solution(N, stages):
    answer = [] # 실패율이 높은 스테이지부터 오름차순
    length = len(stages)
    for i in range(1,N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count/length
        answer.append((i,fail))
        length-=count
    answer=sorted(answer,key=lambda x:x[1], reverse=True)
    result = [x[0] for x in answer]
    return result