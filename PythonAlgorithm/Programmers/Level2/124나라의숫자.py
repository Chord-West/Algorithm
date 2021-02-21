def solution(n):
    a=[]
    while n>0:
        if n%3==0:
            n=n//3-1
            a.insert(0,'4')
        else:
            a.insert(0,str(n%3))
            n=n//3
    answer = ''.join(a)
    return answer