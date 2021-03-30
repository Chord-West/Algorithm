import sys
sys.stdin = open("input.txt","rt")

n,m = sys.stdin.readline().split()
p=dict()

for _ in range(int(n)):
    x=input()
    p[x]=p.get(x,0)+1
for _ in range(int(m)):
    x = input()
    p[x]=p.get(x,0)+1

ans = [ k for k,v in p.items() if v>1]
ans.sort()
print(len(ans))
for x in ans:
    print(x)