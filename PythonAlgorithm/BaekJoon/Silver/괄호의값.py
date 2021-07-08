import sys
sys.stdin = open("input.txt","rt")

brackets = input().rstrip('\n')
stack=[]
ans=0
for x in brackets:
    if x==')':
        tmp_num=0
        while stack:
            top = stack.pop()
            if top=='(':
                if tmp_num==0:
                    stack.append(2)
                else:
                    stack.append(2*tmp_num)
                break
            elif top =='[':
                print(0)
                exit(0)
            else:
                tmp_num = tmp_num+int(top)

    elif x == ']':
        tmp_num = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if tmp_num == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp_num)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                tmp_num = tmp_num + int(top)
    else:
        stack.append(x)

for s in stack:
    if s=='(' or s=='[':
        print(0)
        exit(0)
    else:
        ans+=s