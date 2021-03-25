import sys

sys.stdin = open("input.txt","rt")

for _ in range(int(sys.stdin.readline())):
    arr = input()
    stack=[]
    for x in arr:
        if x =='(':
            stack.append(x)
        elif x == ')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(x)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')