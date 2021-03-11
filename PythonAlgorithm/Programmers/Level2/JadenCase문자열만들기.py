def solution(s):
    answer = ''
    s=s.lower()
    l = s.split(' ')
    for i in l:
        i = i.capitalize()
        answer+=i+" "
    return answer[:-1]