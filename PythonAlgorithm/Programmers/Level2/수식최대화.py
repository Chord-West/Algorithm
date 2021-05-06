from collections import deque

def solution(expression):
    answer = 0
    tmp=''
    arr=[]
    for e in expression:
        if e =='-' or e == '+' or e =='*':
            arr.append(int(tmp))
            tmp=''
            arr.append(e)
        else:
            tmp+=e
    else:
        arr.append(int(tmp))
    oper=['*+-','*-+','+*-','+-*','-*+','-+*']
    q = deque(oper)
    while q:
        exp = q.popleft()
        copy_arr = arr[:]
        for e in exp:
            idx=0
            while idx<len(copy_arr):
                if copy_arr[idx] == e:
                    if e == '*':
                        cal = copy_arr[idx-1]*copy_arr[idx+1]
                    elif e == '-':
                        cal = copy_arr[idx-1]-copy_arr[idx+1]
                    else:
                        cal = copy_arr[idx-1]+copy_arr[idx+1]
                    tmp = copy_arr[idx+2:]
                    copy_arr = copy_arr[:idx-1]
                    copy_arr.append(cal)
                    copy_arr+=tmp
                else:
                    idx+=1
        else:
            answer = max(answer, abs(int(copy_arr[0])))

    return answer