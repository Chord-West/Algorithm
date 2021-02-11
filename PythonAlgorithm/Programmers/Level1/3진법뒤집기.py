def solution(n):
    answer = 0
    s=""
    while n>0:
        s+=str(n%3)
        n=n//3
    s=s[::-1]
    for i in range(len(s)):
        answer+=int(s[i])*pow(3,i)
    return answer