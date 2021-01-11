import sys
sys.stdin = open("input.txt","r")

if __name__ == "__main__":
    n,m = map(int,input().split())
    num=list(map(int,str(n)))
    stack=[]
    for x in num:
        while stack and m>0 and stack[-1]<x:
            stack.pop()
            m-=1
        stack.append(x)

    if m!=0:
        stack=stack[:-m]
    res=''.join(map(str,stack))

    # 7823