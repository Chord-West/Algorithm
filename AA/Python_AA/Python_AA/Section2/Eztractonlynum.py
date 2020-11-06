import sys

#sys.stdin=open("input.txt","rt")

str=input()
res=0

for x in str:
    if x.isdecimal():
        res = res*10+int(x)

print(res)

