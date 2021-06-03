import sys
sys.stdin = open("input.txt","rt")
oper=[]
tmp=''
for s in input():
    if s.isdigit():
        tmp+=s
    else:
        oper.append(tmp)
        tmp=''
        oper.append(s)
else:
    oper.append(tmp)
stack=[]
tmp=0
ch=False
for o in oper:
    if ch:
        ch=False
        stack.append(tmp+int(o))
    elif o =='+':
        tmp=int(stack.pop())
        ch=True
    elif o.isdigit():
        stack.append(int(o))
    else:
        stack.append(o)
print(eval(''.join(map(str,stack))))
