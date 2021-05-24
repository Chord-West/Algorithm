def solution(s):
    stack=[]
    for x in s:
        if len(stack)>0 and stack[-1]==x:
            stack.pop()
        else:
            stack.append(x)
    if len(stack)==0:
        return 1
    else:
        return 0
    return answer