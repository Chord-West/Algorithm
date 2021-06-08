import sys
sys.stdin = open("input.txt","rt")
ans=0
n=1
for i in range(1,int(input())+1):
    n*=i
for s in reversed(str(n)):
    if s=='0':
        ans+=1
    else:
        break
print(ans)
