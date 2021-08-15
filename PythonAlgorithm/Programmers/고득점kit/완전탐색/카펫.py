def solution(brown, red):
    answer=[]
    for i in range(1,int(red/2)+2):
        if red%i==0:
            a,b=max(red//i,i),min(red//i,i)
            if 2*a+(b+2)*2==brown:
                answer.append(a+2)
                answer.append(b+2)
                break
    return answer