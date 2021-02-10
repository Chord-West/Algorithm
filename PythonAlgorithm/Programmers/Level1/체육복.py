def solution(n, lost, reserve):
    answer = 0
    stu = [1]*n
    dir=[-1,1]
    for x in lost:
        stu[x-1]-=1
    for y in reserve:
        stu[y-1]+=1
    for i in range(n):
        if stu[i]==2:
            for x in dir:
                nx = i+x
                if 0<=nx<n and stu[nx]==0 and stu[i]==2:
                    stu[i]-=1
                    stu[nx]+=1
    for x in stu:
        if x>0:
            answer+=1
    return answer