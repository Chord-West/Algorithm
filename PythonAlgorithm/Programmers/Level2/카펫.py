def solution(brown, yellow):
    answer = []
    total = brown + yellow
    li=[[max(total//i,i),min(total//i,i)] for i in range(1,total+1) if total%i==0 ]
    li=li[:len(li)//2+1]
    for bro,yel in li:
        if (bro-1)*2 + (yel-1)*2 == brown:
            answer.append(bro)
            answer.append(yel)
            break
    return answer