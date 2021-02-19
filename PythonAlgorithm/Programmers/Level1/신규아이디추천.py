def solution(dartResult):
    answer =[]
    s=''
    sdt=['S','D','T']
    for x in dartResult:
        if x.isdigit():
            s+=x
        elif x in sdt:
            answer.append(int(s)**(sdt.index(x)+1))
            s=''
        else:
            if x=='*':
                if len(answer)==1:
                    answer[-1]*=2
                else:
                    answer[-2]*=2
                    answer[-1]*=2
            else:
                answer[-1]*=(-1)
    return sum(answer)