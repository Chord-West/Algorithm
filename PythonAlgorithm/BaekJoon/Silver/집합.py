import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline

S=[]
s = [i for i in range(1,21)]

for _ in range(int(r())):
    str=r().split()
    if str[0]=='add':
        if int(str[1]) not in S:
            S.append(int(str[1]))
    elif str[0] == 'check':
        if int(str[1]) in S:
            print(1)
        else:
            print(0)
    elif str[0] == 'remove':
        if int(str[1]) in S:
            S.pop(S.index(int(str[1])))
    elif str[0] == 'toggle':
        if int(str[1]) in S:
            S.pop(S.index(int(str[1])))
        else:
            S.append(int(str[1]))
    elif str[0] == 'all':
        S=s
    else: #empty
        S=[]

