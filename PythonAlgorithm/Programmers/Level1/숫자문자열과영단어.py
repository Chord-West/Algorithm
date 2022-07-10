# 내풀이
def solution(s):
    answer = ''
    p = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
         'five':'5','six':'6','seven':'7','eight':'8','nine':'9' }
    tmp=''
    for word in s:
        if word.isdigit():
            answer+=word
        else:
            tmp+=word
            if tmp in p:
                answer+=p[tmp]
                tmp=''
    return int(answer)
# 다른 사람 풀이
def solution(s):
    answer = ''
    p = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
         'five':'5','six':'6','seven':'7','eight':'8','nine':'9' }
    for key,value in p.items():
        s = s.replace(key,value)
    return int(s)