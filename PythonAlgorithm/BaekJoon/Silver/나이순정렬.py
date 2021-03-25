import sys
sys.stdin = open("input.txt","rt")
n= int(input())
arr = []
for i in range(n):
    age,name= input().split()
    arr.append([int(age),name])
arr = sorted(arr,key=lambda x:x[0])

for x,y in arr:
    print('%s %s' %(x,y))
