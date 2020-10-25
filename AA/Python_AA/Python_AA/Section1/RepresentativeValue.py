import sys

sys.stdin=open("input.txt","rt")

n = int(input())
grade=list(map(int,input().split()))
arrMin=float("inf")
mean=0
for i in range(len(grade)):
    mean+=grade[i]

mean = round(mean/n,0)
print(mean)
