def solution(s):
    answer = True
    stack = []
    for brace in s:
        if brace == '(':
            stack.append(brace)
        else:
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(brace)
    return False if len(stack)>0 else True