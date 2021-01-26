#import sys
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    s=input()
    num=[]
    stack=[]
    for i in range(len(s)):
        if s[i].isdigit():
            num.append(s[i])
        else:
            if s[i]=='*' or s[i]=='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'):
                    num.append(stack.pop())
                stack.append(s[i])
            elif s[i]=='+' or s[i]=='-':
                while stack and stack[-1]!='(':
                    num.append(stack.pop())
                stack.append(s[i])
            elif s[i]=='(':
                stack.append(s[i])
            elif s[i] == ')':
                while stack and stack[-1]!='(':
                    num.append(stack.pop())
                stack.pop()
    while stack:
        num.append(stack.pop())
    res=''.join(map(str,num))
    print(res)