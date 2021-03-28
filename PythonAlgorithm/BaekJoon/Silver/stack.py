import sys
sys.stdin = open("input.txt","rt")

stack=[]
for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    if x[0]=='push':
        stack.append(int(x[1]))
    elif x[0]=='top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
    elif x[0]=='size':
        print(len(stack))
    elif x[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif x[0]=='pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
