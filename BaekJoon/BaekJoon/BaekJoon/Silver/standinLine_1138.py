import sys

sys.stdin = open("input.txt","rt")


n = int(input())
m = list(map(int , input().split()))

line =[n]

for i in range(n-2,-1,-1):
    line.insert(m[i],i+1)
   
for x in line:
    print(x , end=" ")