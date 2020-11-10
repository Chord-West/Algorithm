import sys
sys.stdin = open("input.txt","rt")

s = input()
res=int(s[0])

for i in range(1,len(s)):
    if res*int(s[i] )<res+int(s[i]):
        res+=int(s[i])
    else:
        res*=int(s[i])

print(res)