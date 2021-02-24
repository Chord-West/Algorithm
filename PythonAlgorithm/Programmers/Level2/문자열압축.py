def solution(s):
    answer = len(s)
    for cut in range(1,len(s)):
        count=1
        STR=''
        splited = [s[i:i+cut] for i in range(0,len(s),cut)]
        stack=[[splited[0],1]]
        for unit in splited[1:]:
            if stack[-1][0] != unit:
                stack.append([unit,1])
            else:
                stack[-1][count]+=1
        STR=''.join([str(cnt)+w if cnt>1 else w for w,cnt in stack])
        answer=min(answer,len(STR))
    return answer