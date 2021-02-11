def solution(a, b):
    answer = ''
    months=[31,29,31,30,31,30,31,31,30,31,30]
    days=['THU','FRI','SAT','SUN','MON','TUE','WED']
    sum=0
    for i in range(a-1):
        sum+=months[i]
    sum+=b
    answer=days[sum%7]
    return answer