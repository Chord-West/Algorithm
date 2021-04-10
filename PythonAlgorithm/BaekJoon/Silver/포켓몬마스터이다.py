import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline
n ,m = map(int,r().split())

p = {}
s = ['0']
for i in range(1,n+1):
    x = r().rstrip('\n')
    p[x]=i
    s.append(x)
print(p)
for _ in range(m):
    x = r().rstrip('\n')
    if x.isdigit():
        x=int(x)
        print(s[x])
    else:
        print(p[x])
